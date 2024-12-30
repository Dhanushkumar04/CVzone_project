import cvzone
import cv2

fpsReader = cvzone.FPS(avgCount=30)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)

while True:
    success, img = cap.read()
    print(fpsReader)
    fps , img = fpsReader.update(img,(0,200))
    print(fps)
    cv2.imshow("Image", img)

    cv2.waitKey(1)