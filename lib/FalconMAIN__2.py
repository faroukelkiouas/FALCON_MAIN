import RPi.GPIO as gpio
import cv2
from matplotlib.pyplot import text
import numpy as np
import Falcon
import imutils
import time

en1=20
en2=21
in1=17
in2=22
in3=23
in4=24
gpio.setmode(gpio.BCM)
gpio.setup(in1, gpio.OUT)
gpio.setup(in2, gpio.OUT)
gpio.setup(in3, gpio.OUT)
gpio.setup(in4, gpio.OUT)
gpio.setup(en1,gpio.OUT)
gpio.setup(en2,gpio.OUT)
#pwm1=gpio.PWM(en1,100)
#pwm2=gpio.PWM(en2,100)


W=640
H=480
hW=W/2
hH=H/2


T=80#Tracking-box Tolerance:
CDT=2 #Color Detection Tolerance
min_speed=55
max_speed=60
    
SpeakBlue=0
SpeakRed=0
SpeakGreen=0

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, H)
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
Falcon.SpeakBegin()
Falcon.FrontLight()
#Falcon.Homing()
Falcon.ArmCameraStart()


while True:
    success, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Blue =(LH_B, LS_B, LV_B, HH_B, HS_B, HV_B)
    Blue =(105, 121, 116, 122, 236, 255)
    #Red =(LH_R, LS_R, LV_R, HH_R, HS_R, HV_R)
    Red =(150, 99, 152, 169, 214, 255)
    print(Red)
    #Green =(LH_G, LS_G, LV_G ,HH_G, HS_G, HV_G)
    Green =( 55, 126, 162, 82, 254, 255)
    
    # blue color
    low_blue = np.array([Blue[0], Blue[1], Blue[2]])
    high_blue = np.array([Blue[3], Blue[4], Blue[5]])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    # red color
    low_red = np.array([Red[0], Red[1], Red[2]])
    high_red = np.array([Red[3], Red[4], Red[5]])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    # green color
    low_green = np.array([Green[0], Green[1], Green[2]])
    high_green = np.array([Green[3], Green[4], Green[5]])
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
    #print (x, y, w, h)
    x11 = W-(hW+T)
    y11 = H-(hH+T)
    x22 = W-(hW-T)
    y22 = H-(hH-T)
    
    x_distance = hW-x_medium
    y_distance = hH-y_medium
    new_speed=int(min_speed+((max_speed-min_speed) * abs(x_distance) /hW))
    speed= int(((new_speed-min_speed) / (max_speed-min_speed))* 100)
    
    print("xdis is: ",x_distance)
    print("ydis is: ",y_distance)
    print("New speed is: ",new_speed)
    #print("Speed is: ",str(speed)+ "%")
    #print(X1,Y1,X2,Y2)
    #print(x11,y11,x22,y22)
  

    pt1 = (X1, Y1)
    pt2 = (X2, Y2)
    pt11 = (x11, y11)
    pt22 = (x22, y22)

    cv2.line(frame, (x_medium, 0), (x_medium, 10*W), (0, 255, 0), 4)
    cv2.line(frame, (0, y_medium), (10*H, y_medium), (255, 0, 0), 4)
    
# pick pixel Center color
    pixel_center = frame[int(x_distance), int(y_distance)]
    cv2.circle(frame, (int(x_distance), int(y_distance)), 5, (255, 255, 255), -1)
    print(pixel_center[0],pixel_center[1],pixel_center[0])
    #pixel_center = frame[x_medium, y_medium]
    cv2.circle(frame, (x_medium, y_medium), 5, (0, 0, 255), -1)
    #print("Center Pixel is: ",pixel_center)
            

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
    
        
    if (-T< x_distance < T)and(y_distance > T):
        Falcon.Forward(new_speed) 
        print("FORWARD")
        
    elif (-T< x_distance < T)and(y_distance < -T):
        Falcon.Backward(new_speed)
        print("BACKWARD")
        
    elif (x_distance > T)and((y_distance > T)or(y_distance < T)):
        Falcon.TurnLeft(new_speed,max_speed)
        print("LEFT")
        
    elif (X1 > x11)and(x_distance < T)and((y_distance > T)or(y_distance < T)):       
        Falcon.TurnRight(new_speed,max_speed)    
        print("RIGHT")
   
                 
    elif ( x_distance < T):         
         Falcon.Stop()
         print("STOP")
         Falcon.Speak("Stop")
         Falcon.BackLight()
         time.sleep(2)
         continue
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", blue_mask + red_mask + green_mask )
    cv2.resizeWindow("Frame", W, H)
    cv2.resizeWindow("Mask", W, H)
    key = cv2.waitKey(1)

    if key == 27:
        break
print("Center Pixel is: ",pixel_center)
if ( Blue[2]-CDT< pixel_center[2] < Blue[5]+CDT):
    print("Blueeeeeeee")
    SpeakBlue=1


elif ( Red[2]-CDT< pixel_center[2] < Red[5]+CDT):
    print("Piiiiiiiiink")
    SpeakRed=1

elif (Green[2]-CDT< pixel_center[2] < Green[5]+CDT):
    print("Greeeeeeenn")
    SpeakGreen=1
                   
print("mmmmmmmmmmmmmmmmmmmmmmm")
print("blue is >>",SpeakBlue)
print("red is >>",SpeakRed)
print("green is >>",SpeakGreen)

if(SpeakBlue==1):
    Falcon.Speak("The Color is Blue")
    print("Blue")
if(SpeakRed==1):
    print("Pink")
    Falcon.Speak("The Color is Pink")
if(SpeakGreen==1):
    Falcon.Speak("The Color is Green")
    print("Green")
    
Falcon.angles = Falcon.IK(x=31,y=10,z=500)
#Falcon.angles = Falcon.IK(x=21,y=16,z=20)
print(Falcon.angles)
Falcon.ArmIk(a=Falcon.angles[0],b=Falcon.angles[1] ,c=Falcon.angles[2] ,d=Falcon.angles[3] ,e=Falcon.angles[4], f=70)
time.sleep(2)
Falcon.ArmIk(a=Falcon.angles[0],b=Falcon.angles[1] ,c=Falcon.angles[2] ,d=Falcon.angles[3] ,e=Falcon.angles[4], f=0)
time.sleep(2)
print("PICKED")
Falcon.ArmIk(a=Falcon.angles[0],b=90,c=Falcon.angles[2] ,d=Falcon.angles[3] ,e=90, f=0)
print("DONE")
Falcon.ArmCameraStart()
time.sleep(20)
cv2.destroyAllWindows()

