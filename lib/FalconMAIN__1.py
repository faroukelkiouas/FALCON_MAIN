from ast import And
import cv2
from matplotlib.pyplot import text
import numpy as np
import Falcon
import imutils
import time
tm=0.5

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 64.0)
cap.set(cv2.CAP_PROP_EXPOSURE, 126.0)
cap.set(cv2.CAP_PROP_SATURATION, 55.0)
cap.set(cv2.CAP_PROP_CONTRAST, 4.0)
cap.set(cv2.CAP_PROP_GAIN, -1.0)

success, frame = cap.read()
rows, cols, _ = frame.shape
x_medium = int(cols / 2)
y_medium = int(rows / 2)
center = int(cols / 2)

print("Detecting,,")
Falcon.ArmHoming()
time.sleep(0.1)
Falcon.ArmHoming()
time.sleep(0.1)
Falcon.ArmHoming()
time.sleep(0.2)
Falcon.ArmCamera()

while True:
    success, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Region:
    R = 80
    # blue color
    low_blue = np.array([100, 224, 18])
    high_blue = np.array([116, 255, 18])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    # red color
    low_red = np.array([106, 83, 99])
    high_red = np.array([179, 233, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    # green color
    low_green = np.array([46, 166, 102])
    high_green = np.array([85, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)

    contours, hierarchy = cv2.findContours(
        green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)

        x_medium = int((x + x + w) / 2)
        y_medium = int((y + y + h) / 2)
        break

    X1 = x
    Y1 = y
    X2 = x + w
    Y2 = y + h
    #print (x, y, w, h)
    x11 = 252
    x22 = 377
    y11 = 192
    y22 = 305

    pt1 = (X1, Y1)
    pt2 = (X2, Y2)
    pt11 = (x11, y11)
    pt22 = (x22, y22)

    cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 4)
    cv2.line(frame, (0, y_medium), (720, y_medium), (255, 0, 0), 4)
# pick pixel color
    #pixel_center = frame[x_medium, y_medium]
    #cv2.circle(frame, (x_medium, y_medium), 5, (0, 0, 255), -1)
    #print(pixel_center)
    #if 110 < pixel_center[0] < 170:
    #    print("Blue")
     #   cv2.putText(
      #      frame,
       #     ">>> Blue",
        #    (30, 470),
         #   cv2.FONT_HERSHEY_DUPLEX,
          #  1,
           # (255, 0, 0),
            #4,
        #)

    cv2.rectangle(
        frame,
        (int(pt1[0]), int(pt1[1])),
        (int(pt2[0]), int(pt2[1])),
        color=(255, 255, 255),
        thickness=3,
    )
    cv2.rectangle(
        frame,
        (int(pt11[0]), int(pt11[1])),
        (int(pt22[0]), int(pt22[1])),
        color=(0, 0, 255),
        thickness=3,
    )

   
    if (x11 < x < x22 - w) and (y11 < y < y22 - h):
        Falcon.Forward()
        print("FORWARD")
        
    elif (x11 - R < x < x11 + R) and (y11 - R < y < y11 + R):
        Falcon.Stop()
        print("STOP")
        

    elif x < x11 - R:
        Falcon.TurnLeft()
        print("LEFT")
        
    elif x > x11 + R:
        Falcon.TurnRight()
        print("RIGHT")
        
    if (
        (y > y11 + h + R)
        or ((x11 + R < x < x11 + R) and (y11 + R < y < y11 + R))
        or ((y < y11) and (y22 < Y2))
    ):
        Falcon.Backward()
        print("BACKWARD")
        
    if (y < y11 - R) and (Y2 < y22):
        Falcon.Forward()
        print("FORWARD")
        
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", green_mask )
    cv2.resizeWindow("Frame", 640, 480)
    cv2.resizeWindow("Mask", 640, 480)

    key = cv2.waitKey(1)

    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
