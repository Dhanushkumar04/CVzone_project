import cv2
import cvzone

cap = cv2.VideoCapture(0)

while True:
    success , img = cap.read()
    imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    imgSmall = cv2.resize(img,(0,0),None,0.1,0.1)
    imgBig = cv2.resize(img,(0,0),None,3,3)
    imgCanny = cv2.Canny(img,50,100)
    imgList = [img,imgGray,imgSmall,imgHSV,imgBig,imgCanny,
               img, imgGray, imgSmall, imgHSV, imgBig, imgCanny,
               img, imgGray, imgSmall, imgHSV, imgBig, imgCanny,
               img, imgGray, imgSmall, imgHSV, imgBig, imgCanny,
               img, imgGray, imgSmall, imgHSV, imgBig, imgCanny,
               img, imgGray, imgSmall, imgHSV, imgBig, imgCanny
               ]
    stackedImage = cvzone.stackImages(imgList,cols=12,scale=0.3)
    cv2.imshow("stackedImage",stackedImage)
    #cv2.imshow("img",img)
    cv2.waitKey(1)
