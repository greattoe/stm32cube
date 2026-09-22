import cv2
import numpy as np
import serial
import time

sp = serial.Serial('COM3', 9600, timeout=1)
margin_x = 90
margin_y = 80
step = 1
pan = _pan = tlt = _tlt = 90
sp.write(("pan" + str(pan) + "\n").encode())
sp.write(("tlt" + str(tlt) + "\n").encode())


def main(args=None):
    global pan, _pan, tlt, _tlt  # 전역 변수를 함수 내에서 사용하기 위해 global 선언

    cap = cv2.VideoCapture(0)  # 2번 카메라

    while True:
        time.sleep(0.05)
        ret, frame = cap.read()  # 카메라 프레임 읽기

        if not ret:
            print("카메라에서 프레임을 읽을 수 없습니다.")
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # BGR에서 HSV로 변환

        # 파란색의 HSV 범위 정의
        lower_blue = np.array([100, 100, 120])
        upper_blue = np.array([150, 255, 255])

        lower_green = np.array([50, 150, 50])  # 초록색 범위
        upper_green = np.array([80, 255, 255])

        lower_red = np.array([150, 50, 50])  # 빨간색 범위
        upper_red = np.array([180, 255, 255])

        # HSV 이미지에서 파란색을 추출
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        mask1 = cv2.inRange(hsv, lower_green, upper_green)
        mask2 = cv2.inRange(hsv, lower_red, upper_red)

        # 마스크를 원본 이미지에 적용
        res1 = cv2.bitwise_and(frame, frame, mask=mask)
        res = cv2.bitwise_and(frame, frame, mask=mask1)
        res2 = cv2.bitwise_and(frame, frame, mask=mask2)

        gray = cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)
        _, bin = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        largest_contour = None
        largest_area = 0

        COLOR = (0, 255, 0)
        for cnt in contours:  # 가장 큰 파란색 객체를 찾습니다.
            area = cv2.contourArea(cnt)
            if area > largest_area:
                largest_area = area
                largest_contour = cnt

        # 외곽선을 그립니다.
        if largest_contour is not None:
            if largest_area > 500:  # 500보다 큰 객체에 대해서만 작업 수행
                x, y, width, height = cv2.boundingRect(largest_contour)
                center_x = x + width // 2
                center_y = y + height // 2
                print("center: ( %s, %s )" % (center_x, center_y))

                
                '''---------------------------------------------------'''
                if center_y <= 240 - margin_y:  # tlt-- fot tilt down
                    if tlt + step >= 0:
                        tlt = tlt - step
                    else:
                        tlt = 0
                    _tlt = tlt
                elif center_y > 240 + margin_y:  # tlt++ for tilt up
                    if tlt + step <= 180:
                        tlt = tlt + step
                    else:
                        tlt = 180
                    _tlt = tlt
                else:  # fix tlt value for stop tilt
                    tlt = _tlt
                sp.write(("tlt" + str(tlt) + "\n").encode())

                cv2.rectangle(frame, (x, y), (x + width, y + height), COLOR, 2)
                time.sleep(0.05)

        cv2.imshow("VideoFrame", frame)  # 원본 프레임 출력

        k = cv2.waitKey(5) & 0xFF
        if k == 27:  # ESC 키를 누르면 종료
            break

    cap.release()  # 카메라 해제
    cv2.destroyAllWindows()  # 모든 창 닫기


if __name__ == "__main__":
    main()
