import cv2
import cvzone

cap = cv2.VideoCapture(0)

imgPNG = cvzone.downloadImageFromUrl('https://github.com/cvzone/cvzone/blob/master/Results/cvzoneLogo.png?raw=true',keepTransparency=True)
#imgPNG = cv2.imread("icon.png",cv2.IMREAD_UNCHANGED)

while True:
    success , img = cap.read()
    imgOverlay = cvzone.overlayPNG(img,imgPNG,[0,25])
    cv2.imshow("ImgOverlay",imgOverlay)
    cv2.waitKey(1)