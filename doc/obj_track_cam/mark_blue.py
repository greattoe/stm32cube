import cv2
import numpy as np

# Open webcam using DirectShow
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Define range of blue color in HSV
lower_blue = np.array([100, 100, 120])
upper_blue = np.array([150, 255, 255])

COLOR = (0, 255, 0)

while True:

    # Read one frame from webcam
    ret, src = cap.read()

    if not ret:
        print("Cannot receive frame")
        break

    # Convert from BGR to HSV
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

    # Make blue mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Apply blue mask
    res = cv2.bitwise_and(src, src, mask=mask)

    # Find contours directly from binary mask
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Find largest blue object
    largest_contour = None
    largest_area = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > largest_area:
            largest_area = area
            largest_contour = cnt

    # Draw bounding box
    if largest_contour is not None:

        if largest_area > 500:

            x, y, width, height = cv2.boundingRect(largest_contour)

            cv2.rectangle(
                src,
                (x, y),
                (x + width, y + height),
                COLOR,
                2
            )

    # Show images
    cv2.imshow("origin", src)
    #cv2.imshow("mask", mask)
    #cv2.imshow("blue", res)

    # ESC key to quit
    k = cv2.waitKey(10) & 0xFF

    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()