import cvzone
from cvzone.PlotModule import LivePlot
import cv2
import math
from cvzone.FaceDetectionModule import FaceDetector
cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetectionCon=0.85, modelSelection=0)
xPlot = LivePlot(w=1200, yLimit=[0, 500], interval=0.01,char="X")

sinPlot = LivePlot(w=1200, yLimit=[-100, 100], interval=0.01,char="S")
xSin=0

while True:
    success,img = cap.read()
    img, bboxs = detector.findFaces(img, draw=False)
    val = 0
    if bboxs:
        # Loop through each bounding box
        for bbox in bboxs:
            # bbox contains 'id', 'bbox', 'score', 'center'
            # ---- Get Data  ---- #
            center = bbox["center"]
            x, y, w, h = bbox['bbox']
            score = int(bbox['score'][0] * 100)
            val = center[0]
            # ---- Draw Data  ---- #
            cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
            cvzone.putTextRect(img, f'{score}%', (x, y - 10))
            cvzone.cornerRect(img, (x, y, w, h))

    imgPlot = xPlot.update(val)
    if xSin == 360: xSin = 0
    imgPlotSin = sinPlot.update(int(math.sin(math.radians(xSin)) * 100))
    imgStacked = cvzone.stackImages([imgPlot,img,imgPlotSin],3,0.3)
    cv2.imshow("ImageStacked", imgStacked)
    #cv2.imshow("Image Sin Plot", imgPlotSin)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


