import cv2
import cvzone
from PIL.ImageChops import offset

cap = cv2.VideoCapture(0)

while True:
    success , img = cap.read()
    cvzone.putTextRect(img,"Dhanush",(0,50),border=5,offset=15)
    cv2.imshow("Image",img)
    cv2.waitKey(1)