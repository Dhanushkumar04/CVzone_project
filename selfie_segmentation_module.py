import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

cap = cv2.VideoCapture(0)

cap.set(3,480)
cap.set(4,480)

segmentor = SelfiSegmentation(model=0)

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img,imgBg=(255,255,0),cutThreshold=0.1)

    imgStacked = cvzone.stackImages([img,imgOut],cols=2,scale=1)

    cv2.imshow("Imagestacked",imgStacked)
    cv2.waitKey(1)