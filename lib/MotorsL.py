import RPi.GPIO as gpio
import time
en1=20
en2=21
in1=17
in2=22
in3=23
in4=24
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(en1,gpio.OUT)
    gpio.setup(en2,gpio.OUT) 
    gpio.setup(in1, gpio.OUT)
    gpio.setup(in2, gpio.OUT)
    gpio.setup(in3, gpio.OUT)
    gpio.setup(in4, gpio.OUT)
def forward(sec):
    init()
    gpio.setup(en1,gpio.OUT)
    gpio.setup(en2,gpio.OUT)
    pwm1=gpio.PWM(en1,100)
    pwm2=gpio.PWM(en2,100)
    pwm1.start(75)
    pwm2.start(75)
    gpio.output(in1, False)
    gpio.output(in2, True)
    gpio.output(in3, False)
    gpio.output(in4, True)
    time.sleep(sec)
    gpio.cleanup() 
def reverse(sec):
    init()
    gpio.output(in1, True)
    gpio.output(in2, False)
    gpio.output(in3, True)
    gpio.output(in4, False)
    time.sleep(sec)
    gpio.cleanup()
def left_turn(sec):
    init()
    gpio.output(in1, False)
    gpio.output(in2, True)
    gpio.output(in3, True)
    gpio.output(in4, False)
    time.sleep(sec)
    gpio.cleanup()
def right_turn(sec):
    init()
    gpio.output(in1, True)
    gpio.output(in2, False)
    gpio.output(in3, False)
    gpio.output(in4, True)
    time.sleep(sec)
    gpio.cleanup()
def stop(sec):
    init()
    gpio.output(in1, False)
    gpio.output(in2, False)
    gpio.output(in3, False)
    gpio.output(in4, False)
    time.sleep(sec)
    gpio.cleanup()
tm=0.5
ts=1
stop(2)
print("forward")
forward(tm)
stop(ts)
print("backward")
reverse(tm)
stop(ts)
print("right")
right_turn(tm)
stop(ts)
print("left")
left_turn(tm)
print("STOP")
stop(4)