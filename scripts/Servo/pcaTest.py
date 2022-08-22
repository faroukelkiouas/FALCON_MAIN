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
pca.frequency = 50

servo0= servo.Servo(pca.channels[0])

t=1
# We sleep in the loops to give the servo time to move into position
while True:
    servo0.angle = 10
    time.sleep(t)
    servo0.angle = 150
    time.sleep(t)

    print("doooooooooneee")



fraction = 0.0
while fraction < 1.0:
    servo1.fraction = fraction
  
    fraction += 90
    time.sleep(0.03)

pca.deinit()

