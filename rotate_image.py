import cv2
from cvzone import rotateImage

cap = cv2.VideoCapture(0)

while True:
    success , img = cap.read()
    imgRotated90 = rotateImage(img,90,scale=1,keepSize=False)
    imgRotated90_ = rotateImage(img,90,scale=1,keepSize=True)

    cv2.imshow("Image",img)
    cv2.imshow("imgRotated90",imgRotated90)
    cv2.imshow("imgRotated90_",imgRotated90_)

    cv2.waitKey(1)