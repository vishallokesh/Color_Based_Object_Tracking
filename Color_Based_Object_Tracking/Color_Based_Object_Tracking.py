
import cv2
import math
import time
from Util import get_limits
from PIL import Image

Red = [25, 0, 255]
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=Red)

    mask = cv2.inRange(hsvImage,  lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        midX = (x2+x1)/2
        midY = (y2+y1)/2
        boxMid = [midX, midY]
        originValue = [360, 203]
        distanceToOrigin = math.dist(boxMid, originValue)
        IMGframe = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        IMGcenter = cv2.rectangle(frame, (int(midX), int(midY)), (int(midX)+1, int(midY)+1), (0, 255, 255), 5)
        origin = cv2.rectangle(frame, (360, 203), (360, 203), (0, 0, 255), 5)
        print('distance to origin is', round(distanceToOrigin, 2))
        cv2.imshow('frame', IMGframe)
        cv2.imshow('frame', origin)
        cv2.imshow('frame', IMGcenter)
    

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release

cv2.destroyAllWindows


