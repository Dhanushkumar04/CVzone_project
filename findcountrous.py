import cv2
import cvzone
import numpy as np

imgShapes=cvzone.downloadImageFromUrl('https://github.com/cvzone/cvzone/blob/master/Results/shapes.png?raw=true')
imgCanny = cv2.Canny(imgShapes,50,100)
imgDilated = cv2.dilate(imgCanny,np.ones((5,5),np.uint8),iterations=1)

imgContours , conFound = cvzone.findContours(imgShapes,imgDilated)
imgContoursFiltered , conFoundFiltered = cvzone.findContours(imgShapes,imgDilated,filter=[3,4])
cv2.imshow("ImgaeCountours",imgContours)
cv2.imshow("ImageContoursFiltered",imgContoursFiltered)
cv2.waitKey(0)