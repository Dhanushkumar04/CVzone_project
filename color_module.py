import cv2
import cvzone


myColorFinder = cvzone.ColorFinder(trackBar=False)
cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,480)
hsVals={'hmin': 0, 'smin': 0, 'vmin': 190, 'hmax': 179, 'smax': 197, 'vmax': 255}

while True:
    success, img = cap.read()
    imgOrange, mask = myColorFinder.update(img,hsVals)
    imgContours, conFound = cvzone.findContours(img,mask)
    imgStack = cvzone.stackImages([img,imgOrange,mask,imgContours],2,0.5)
    cv2.imshow("StackImages",imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break