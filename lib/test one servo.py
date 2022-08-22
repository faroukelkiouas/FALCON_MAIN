# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time

from board import SCL, SDA
import busio


from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)
pca.frequency =50

pca.channels[5].duty_cycle = 0x7FFF
servo1= servo.Servo(pca.channels[0])

servo0= servo.Servo(pca.channels[1])

t=1
# We sleep in the loops to give the servo time to move into position
while True:
    
    servo1.angle = 90
    print("1")    
    servo0.angle =0
    time.sleep(t)
    print("2")
    servo0.angle =0
    time.sleep(t)

pca.deinit()

