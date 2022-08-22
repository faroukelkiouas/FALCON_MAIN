import time
import RPi.GPIO as GPIO

# Import the PCA9685 module.
import Adafruit_PCA9685
# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
i2c = busio.I2C(SCL, SDA)
# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)

pca.frequency = 50
t=0
t1=3
tm=1
s=100

from AMSpi import AMSpi

#Servo Channels:
servo0= servo.Servo(pca.channels[0])
servo1= servo.Servo(pca.channels[1])
servo2= servo.Servo(pca.channels[2])
servo3= servo.Servo(pca.channels[3])
servo4= servo.Servo(pca.channels[4])
servo5= servo.Servo(pca.channels[5])
#LED Channels:
LedR= servo.Servo(pca.channels[8])
LedL= servo.Servo(pca.channels[9])
LedF= servo.Servo(pca.channels[10])
LedB= servo.Servo(pca.channels[11])
#Stting Channels:
Set0= servo.Servo(pca.channels[13])
Set90= servo.Servo(pca.channels[14])
Set180= servo.Servo(pca.channels[15])

# We sleep in the loops to give the servo time to move into position

#Lights:

def FrontLight():
    print ("FRONT LED")    
    pwm.set_pwm(8, 6000, 1500)
    pwm.set_pwm(9, 0, 0)
    pwm.set_pwm(10, 0, 0)
    pwm.set_pwm(11, 0, 0)
    
def BackLight():
    print ("STOP")    
    pwm.set_pwm(8, 0, 0)
    pwm.set_pwm(9, 0, 0)
    pwm.set_pwm(10, 0, 0)
    pwm.set_pwm(11, 6000, 1500)

def RightLight():   
    print ("RIGHT LED")    
    pwm.set_pwm(8, 0, 0)
    pwm.set_pwm(9, 6000, 1500)
    time.sleep(0.5)
    pwm.set_pwm(9, 0, 0)
    time.sleep(0.5)
    pwm.set_pwm(10, 0, 0)
    pwm.set_pwm(11, 0, 0)
    
def LeftLight():   
    print ("LEFT LED") 
    pwm.set_pwm(8, 0, 0)
    pwm.set_pwm(9, 0, 0)
    pwm.set_pwm(10, 6000, 1500)
    time.sleep(0.5)
    pwm.set_pwm(10, 0, 0)
    time.sleep(0.5)
    pwm.set_pwm(11, 0, 0)
        
def ArmHoming():
    print ("HOMING")
    
    # joint 0:
    print("Channel0")
    servo0.angle =90
    time.sleep(t)
    # joint 1:
    print("Channel1")
    servo1.angle =110
    time.sleep(t)
    # joint 2:
    print("Channel2")
    servo2.angle =120
    time.sleep(t)
    # joint 3:
    print("Channel3")
    servo3.angle =90
    time.sleep(t)
    # joint 4:
    print("Channel4")
    servo4.angle =170
    time.sleep(t)
    # joint 5:
    print("Channel5")   
    servo5.angle =10
    time.sleep(0.5)
    servo5.angle =100
    time.sleep(0.5)
def ArmCamera():
    print ("CameraOn")
    
    # joint 0:
    print("Channel0")
    servo0.angle =90
    time.sleep(t)
    # joint 1:
    print("Channel1")
    servo1.angle =110
    time.sleep(t)
    # joint 2:
    print("Channel2")
    servo2.angle =90
    time.sleep(t)
    # joint 3:
    print("Channel3")
    servo3.angle =90
    time.sleep(0.5)
    # joint 4:
    print("Channel4")
    servo4.angle =0
    time.sleep(t)
    # joint 5:
    print("Channel5")
    servo5.angle =10
    
    
def Forward():
    with AMSpi() as amspi:
        # Set PINs for controlling shift register (GPIO numbering)
        amspi.set_74HC595_pins(21, 20, 16)
        # Set PINs for controlling all 4 motors (GPIO numbering)
        amspi.set_L293D_pins(5, 6, 13, 19)
        
        amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4],speed=s)
        time.sleep(tm)
        print("1")
         
def Backward():
    with AMSpi() as amspi:
        # Set PINs for controlling shift register (GPIO numbering)
        amspi.set_74HC595_pins(21, 20, 16)
        # Set PINs for controlling all 4 motors (GPIO numbering)
        amspi.set_L293D_pins(5, 6, 13, 19)
        
        amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4],clockwise=False,speed=s)
        time.sleep(tm)
        print("2")
def TurnRight():
    with AMSpi() as amspi:
        # Set PINs for controlling shift register (GPIO numbering)
        amspi.set_74HC595_pins(21, 20, 16)
        # Set PINs for controlling all 4 motors (GPIO numbering)
        amspi.set_L293D_pins(5, 6, 13, 19)
        
        amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_4],speed=s)
        amspi.run_dc_motors([amspi.DC_Motor_2, amspi.DC_Motor_3],clockwise=False,speed=s)

        time.sleep(tm)
        print("R")
def TurnLeft():
    with AMSpi() as amspi:
        # Set PINs for controlling shift register (GPIO numbering)
        amspi.set_74HC595_pins(21, 20, 16)
        # Set PINs for controlling all 4 motors (GPIO numbering)
        amspi.set_L293D_pins(5, 6, 13, 19)
        
        amspi.run_dc_motors([amspi.DC_Motor_2, amspi.DC_Motor_3],speed=s)
        amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_4],clockwise=False,speed=s)
        time.sleep(tm)
        print("L")
def Stop():
    with AMSpi() as amspi:
        # Set PINs for controlling shift register (GPIO numbering)
        amspi.set_74HC595_pins(21, 20, 16)
        # Set PINs for controlling all 4 motors (GPIO numbering)
        amspi.set_L293D_pins(5, 6, 13, 19)
        amspi.stop_dc_motors([amspi.DC_Motor_1])
        amspi.stop_dc_motors([amspi.DC_Motor_2])
        amspi.stop_dc_motors([amspi.DC_Motor_3])
        amspi.stop_dc_motors([amspi.DC_Motor_4])
def Exit():
    with AMSpi() as amspi:
        # Set PINs for controlling shift register (GPIO numbering)
        amspi.set_74HC595_pins(21, 20, 16)
        # Set PINs for controlling all 4 motors (GPIO numbering)
        amspi.set_L293D_pins(5, 6, 13, 19)
        amspi.__exit__(1,1,1)
        amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])

        time.sleep(2)
def Cleanup():
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    time.sleep(1)
    GPIO.cleanup()
    time.sleep(1)
    GPIO.cleanup()    
    print("CLean")
    

    






        



        


        


      



