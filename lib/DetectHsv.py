import cv2

cap= cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    height,width,_=frame.shape
    
    cx= int(width/2)
    cy = int(height/2)
    
    #Pick Pixel Value:
    pixel_center = frame [cy,cx]
    print(pixel_center)
    cv2.circle(frame,(cx,cy),5,(255,8,8),3)
    
    cv2.imshow("frame",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()