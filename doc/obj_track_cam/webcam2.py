import cv2

webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()

    img = cv2.resize(frame, dsize=(320,240), interpolation=cv2.INTER_AREA)

    if status:
        cv2.imshow("test", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()