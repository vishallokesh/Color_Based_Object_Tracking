
import cv2
import math
from pyfirmata import Board, SERVO
from Util import get_limits
from PIL import Image

Red = [25, 0, 255]
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

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
        originValue = [330, 240]
        distanceToOrigin = math.dist(boxMid, originValue)
        IMGframe = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        IMGcenter = cv2.rectangle(frame, (int(midX), int(midY)), (int(midX)+1, int(midY)+1), (0, 255, 255), 5)
        origin = cv2.rectangle(frame, (330, 240), (330, 240), (0, 0, 255), 5)
        print('x is', round((midX-330)/330, 3), 'distance away ad y is', round((midY-240)/240, 3), 'distance away')
        #print('distance to origin is', round(distanceToOrigin, 2))
        cv2.imshow('frame', IMGframe)
        cv2.imshow('frame', origin)
        cv2.imshow('frame', IMGcenter)
    
    xServo = round((midX-330)/330, 3)
    yServo = round((midY-240)/240, 3)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release

cv2.destroyAllWindows


