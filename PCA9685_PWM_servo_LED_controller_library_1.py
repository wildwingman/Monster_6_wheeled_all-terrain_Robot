#!/usr/bin/python




# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time
from Adafruit_PWM_Servo_Driver import PWM

# Import the PCA9685 module.
#import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = PWM(0x40)

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out oservoMin = 257  # Min pulse length out of 4096
#servoMax = 600  # Max pulse length out of 4096
#servo1Min = 220 # Min pulse length out of 4096
#servo1Max = 785  # Max pulse length out of 4096


# Helper function to make setting a servo pulse width simpler.
def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 10000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
  pwm.setPWMFreq(70)

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
# Move servo on channel O between extremes.
  
  
  pwm.setPWM(15, 0, servoMin)
  pwm.setPWM(0, 1, servoMin)
  #pwm.setPWM(1, 1, servo1Min)
  #pwm.setPWM(2, 0, servoMin)
  #pwm.setPWM(3, 0, servoMin)
  #pwm.setPWM(4, 0, servoMin)
  time.sleep(1)
  pwm.setPWM(15, 0, servoMax)
  pwm.setPWM(0, 1, servoMax)
  #pwm.setPWM(1, 1, servo1Max)
  #pwm.setPWM(2, 0, servoMax)
  #pwm.setPWM(3, 0, servoMax)
  #pwm.setPWM(4, 0, servoMax)
  time.sleep(1)
