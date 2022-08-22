import numpy as np
import cv2

properties=["CAP_PROP_FRAME_WIDTH",# Width of the frames in the video stream.
            "CAP_PROP_FRAME_HEIGHT",# Height of the frames in the video stream.
            "CAP_PROP_BRIGHTNESS",# Brightness of the image (only for cameras).
            "CAP_PROP_CONTRAST",# Contrast of the image (only for cameras).
            "CAP_PROP_SATURATION",# Saturation of the image (only for cameras).
            "CAP_PROP_GAIN",# Gain of the image (only for cameras).
            "CAP_PROP_EXPOSURE"]

cap = cv2.VideoCapture(0)
for prop in properties:
    val=cap.get(eval("cv2."+prop))
    print (prop+": "+str(val))

gain=0
cap.set(cv2.CAP_PROP_GAIN,gain)

brightness=60
cap.set(cv2.CAP_PROP_BRIGHTNESS,brightness)

contrast=20
cap.set(cv2.CAP_PROP_CONTRAST,contrast)

saturation=20
cap.set(cv2.CAP_PROP_SATURATION,saturation)

exposure=-1
cap.set(cv2.CAP_PROP_EXPOSURE,exposure)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb=frame

    print( "\n\n")
    for prop in properties:
        val=cap.get(eval("cv2."+prop))
        print (prop+": "+str(val))
    # Display the resulting frame
    cv2.imshow('frame',rgb)
    key=cv2.waitKey(1)
    if key == ord('x'):
        break
    elif key == ord('w'):
        brightness+=1
        cap.set(cv2.CAP_PROP_BRIGHTNESS,brightness)
    elif key == ord('s'):
        brightness-=1
        cap.set(cv2.CAP_PROP_BRIGHTNESS,brightness)
    elif key == ord('d'):
        contrast+=1
        cap.set(cv2.CAP_PROP_CONTRAST,contrast)
    elif key == ord('a'):
        contrast-=1
        cap.set(cv2.CAP_PROP_CONTRAST,contrast)
    elif key == ord('e'):
        saturation+=1
        cap.set(cv2.CAP_PROP_SATURATION,saturation)
    elif key == ord('q'):
        saturation-=1
        cap.set(cv2.CAP_PROP_SATURATION,saturation)
    elif key == ord('z'):
        exposure+=1
        cap.set(cv2.CAP_PROP_EXPOSURE,exposure)
    elif key == ord('c'):
        exposure-=1
        cap.set(cv2.CAP_PROP_EXPOSURE,exposure)

# When everything done, release the capture
cap.release()
#cv2.destroyAllWindows()