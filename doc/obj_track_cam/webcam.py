import cv2

# step2.카메라 열기 - 0은 기본 카메라를 의미
cap = cv2.VideoCapture(0)

# step3.무한 반복
while True:
    # 카메라 연결 여부(True/False)와 현재 프레임 이미지를 읽음
    retval, frame = cap.read()
    
    # 만약 카메라가 연결되어 있지 않으면 while 반복문 종료
    if retval == False:
        break
    
    # 'frame'이란 창 이름으로 현재 프레임 출력
    cv2.imshow('frame', frame)

    # 10초가 지나거나, ESC 키가 입력되면 while 반복문 종료
    if cv2.waitKey(10) == 27:
        break

# step4.카메라 닫고 모든창 종료
cap.release()

cv2.destroyAllWindows()