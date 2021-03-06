#!/usr/bin/python

import curses
from Adafruit_PWM_Servo_Driver import PWM
# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=False)

servoMin = 160  # Min pulse length out of 4096
servoMax = 400  # Max pulse length out of 4096
maxDegree = 60 # Degrees your servo can rotate
degIncrease = 2 # Number of degrees to increase by each time

servoMin1 = 180  # Min pulse length out of 4096
servoMax1 = 475  # Max pulse length out of 4096
maxDegree1 = 60 # Degrees your servo can rotate
degIncrease1 = 2 # Number of degrees to increase by each time

servoMin2 = 180  # Min pulse length out of 4096
servoMax2 = 300  # Max pulse length out of 4096
maxDegree2 = 60 # Degrees your servo can rotate
degIncrease2 = 2 # Number of degrees to increase by each time

servoMin3 = 180  # Min pulse length out of 4096
servoMax3 = 300  # Max pulse length out of 4096
maxDegree3 = 60 # Degrees your servo can rotate
degIncrease3 = 2 # Number of degrees to increase by each time



pwm.setPWMFreq(60) # Set PWM frequency to 60Hz

def servo(channel, d):
    degreePulse = servoMin
    degreePulse += int((servoMax - servoMin) / maxDegree) * d
    pwm.setPWM(channel, 0, degreePulse)
def servo1(channel, d):
    degreePulse1 = servoMin1
    degreePulse1 += int((servoMax1 - servoMin1) / maxDegree1) * d
    pwm.setPWM(channel, 0, degreePulse1)
def servo2(channel, d):
    degreePulse2 = servoMin2
    degreePulse2 += int((servoMax2 - servoMin2) / maxDegree2) * d
    pwm.setPWM(channel, 0, degreePulse2)
    
# Set up curses for arrow input
scr = curses.initscr()
curses.cbreak()
scr.keypad(1)
scr.addstr(0, 0, "Pan & Tilt Control")
scr.addstr(1, 0, "LEFT to Pan Left")
scr.addstr(2, 0, "RIGHT to Pan Right")
scr.addstr(3, 0, "UP to Tilt Up")
scr.addstr(4, 0, "DOWN to Tilt Down")
scr.addstr(5, 0, "Arm Up  o")
scr.addstr(6, 0, "Arm Up  l")
scr.addstr(7, 0, "q to quit")
scr.refresh()

degree = 60 
degree1 = 60 
degree2 = 60 

servo(0, degree)
servo1(1, degree1)
servo2(2, degree2)

key = ''
while key != ord('q'):
    key = scr.getch()

    if key == curses.KEY_RIGHT:
        degree += degIncrease

        if degree > 600:
           degree = 50
        servo(0, degree)
    elif key == curses.KEY_LEFT:
       degree -= degIncrease

       if degree > 660:
          degree = 50
       servo(0, degree)

    elif key == curses.KEY_UP:
       degree1 += degIncrease

       if degree1 > 4000:
          degree1 = 1000
       servo1(1, degree1)

    elif key == curses.KEY_DOWN:
       degree1 -= degIncrease

       if degree1 > 4000:
          degree1 = -1000
       servo1(1, degree1)

    elif key != ord('o'):
       #key = scr.getch()
       degree2 += degIncrease

       if degree2 > 4000:
          degree2 = 1000
       servo2(2, degree2)

    elif key != ord('l'):
       #key = scr.getch()
       degree2 -= degIncrease

       if degree2 > 4000:
          degree2 = -1000
       servo2(2, degree2)
       

curses.endwin()
