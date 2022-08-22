from ast import And
from tkinter import Y
import cv2
from matplotlib.pyplot import text
import numpy as np
import time

cap = cv2.VideoCapture(0)

# grab the width, height, and fps of the frames in the video stream.
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))




success, frame = cap.read()
rows, cols, _ = frame.shape
x_medium = int(cols / 2)
y_medium = int(rows / 2)
center = int(cols / 2)

while True:
    success, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # blue color
    low_blue = np.array([98, 214, 0])
    high_blue = np.array([169, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    # red color
    low_red = np.array([196, 0, 0])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    # green color
    low_green = np.array([49, 184, 46])
    high_green = np.array([89, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)

    contours, hierarchy = cv2.findContours(
        blue_mask + red_mask + green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
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

    x11 = 200
    x22 = 420
    y11 = 140
    y22 = 360

    pt1 = (X1, Y1)
    pt2 = (X2, Y2)
    pt11 = (x11, y11)
    pt22 = (x22, y22)

    cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 4)
    cv2.line(frame, (0, y_medium), (720, y_medium), (255, 0, 0), 4)
    # pick pixel color
    pixel_center = frame[x_medium, y_medium]
    cv2.circle(frame, (x_medium, y_medium), 5, (0, 0, 255), -1)
    print(pixel_center)
    if 110 < pixel_center[0] < 170:
        print("Blue")
        cv2.putText(
            frame,
            ">>> Blue",
            (30, 470),
            cv2.FONT_HERSHEY_DUPLEX,
            1,
            (255, 0, 0),
            4,
        )

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

    # Using cv2.putText()
    cv2.putText(
        frame,
        ">>>Falcon is detecting...",
        (30, 30),
        cv2.FONT_HERSHEY_DUPLEX,
        1,
        (20, 0, 200),
        2,
    )
    cv2.putText(
        img=frame,
        text="x:" + str(x) + " y:" + str(y) + " w:" + str(w) + " h:" + str(h),
        org=(70, 70),
        fontFace=cv2.FONT_HERSHEY_DUPLEX,
        fontScale=0.8,
        color=(200, 200, 200),
        thickness=2,
    )
    R = 20
    if (x11 < x < x22 - w) and (y11 < y < y22 - h):
        cv2.putText(
            img=frame,
            text="In Zone Go Forward!",
            org=(150, 130),
            fontFace=cv2.FONT_HERSHEY_DUPLEX,
            fontScale=1,
            color=(0, 0, 200),
            thickness=4,
        )

    elif (x11 - R < x < x11 + R) and (y11 - R < y < y11 + R):
        cv2.putText(
            img=frame,
            text="STOP",
            org=(270, 130),
            fontFace=cv2.FONT_HERSHEY_DUPLEX,
            fontScale=1,
            color=(0, 0, 200),
            thickness=4,
        )

    elif x < x11 - R:
        cv2.putText(
            img=frame,
            text="RIGHT",
            org=(440, 250),
            fontFace=cv2.FONT_HERSHEY_DUPLEX,
            fontScale=1,
            color=(0, 200, 0),
            thickness=3,
        )
    elif x > x11 + R:
        cv2.putText(
            img=frame,
            text="LEFT",
            org=(100, 250),
            fontFace=cv2.FONT_HERSHEY_DUPLEX,
            fontScale=1,
            color=(0, 200, 0),
            thickness=3,
        )
    if (
        (y > y11 + h + R)
        or ((x11 + R < x < x11 + R) and (y11 + R < y < y11 + R))
        or ((y < y11) and (y22 < Y2))
    ):
        cv2.putText(
            img=frame,
            text="BACKWARD",
            org=(230, 400),
            fontFace=cv2.FONT_HERSHEY_DUPLEX,
            fontScale=1,
            color=(200, 0, 0),
            thickness=3,
        )
    if (y < y11 - R) and (Y2 < y22):
        cv2.putText(
            img=frame,
            text="FORWARD",
            org=(240, 125),
            fontFace=cv2.FONT_HERSHEY_DUPLEX,
            fontScale=1,
            color=(200, 0, 0),
            thickness=3,
        )
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", green_mask + blue_mask + red_mask)
    cv2.resizeWindow("Frame", 640, 480)
    cv2.resizeWindow("Mask", 640, 480)

    key = cv2.waitKey(1)

    if key == 27:
        break
output.release()
cap.release()
cv2.destroyAllWindows()
