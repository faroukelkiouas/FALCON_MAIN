import pty
import tty,sys, termios
import time

# Import the PCA9685 module.
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()

pid = pty.fork()
if not pid:
    # is child
    termios.tcgetattr(sys.stdin.fileno())
    tty.setcbreak(sys.stdin)
x = 0
while 1:
  x=sys.stdin.read(1)[0]
  print("You pressed", x)
  if x == "f":
    print("Front lights ON")
    while True:
        pwm.set_pwm(8, 6000, 1500)
  elif x == "b":
    print("Back lights ON")
    while True:
        pwm.set_pwm(8, 6000, 1500)
        
        
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, filedescriptors)
