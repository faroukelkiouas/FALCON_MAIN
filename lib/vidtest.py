import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        assert not isinstance(frame,type(None)), 'frame not found'
