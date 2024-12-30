import cv2
from cvzone import cornerRect

cap = cv2.VideoCapture(0)


while True:
    success , img = cap.read()
    #cv2.rectangle(img, (200, 200), (500, 400), (255,0,255), 3)

    cornerRect(img,(200,200,300,200),l=30,t=10,rt=2,colorR=(255,0,255),colorC=(0,255,0))

    cv2.imshow("Image",img)
    cv2.waitKey(1)