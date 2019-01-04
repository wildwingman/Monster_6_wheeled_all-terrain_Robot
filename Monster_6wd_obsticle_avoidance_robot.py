#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import RPi.GPIO as gpio
import time

import atexit
import sys
import Tkinter as tk

gpio.setwarnings(False)

gpio.setmode(gpio.BCM)
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.IN)

print "ultrasonic Measurement"
gpio.output(23, 0)

def mr():
  time.sleep(0.333)
  gpio.output(23, 1)
  time.sleep(0.00001)
  gpio.output(23, 0)
  start = time.time()

  while gpio.input(24) == 0:
    start = time.time()
    
  while gpio.input(24) == 1:
    stop = time.time()    

  el = stop - start
  dis = (el * 34300)/2
  
  return dis

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)
mh1 = Adafruit_MotorHAT(addr=0x61)

# recommended for auto-disabling motors on shutdown!
def allStop():
    mh1.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh1.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh1.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh1.getMotor(4).run(Adafruit_MotorHAT.RELEASE) 
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
    
atexit.register(allStop)


################################# DC motor test!
myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(2)
myMotor3 = mh.getMotor(3)
myMotor4 = mh.getMotor(4)
myMotor5 = mh1.getMotor(1)
myMotor6 = mh1.getMotor(2)
myMotor7 = mh1.getMotor(3)
myMotor8 = mh1.getMotor(4)

myMotor1.setSpeed(100)
myMotor2.setSpeed(100)
myMotor3.setSpeed(100)
myMotor4.setSpeed(100)
myMotor5.setSpeed(100)
myMotor6.setSpeed(100)
myMotor7.setSpeed(100)
myMotor8.setSpeed(100)


def moveForward():
        print "Move Forward"
        myMotor1.run(Adafruit_MotorHAT.FORWARD);
        myMotor2.run(Adafruit_MotorHAT.FORWARD);
        myMotor3.run(Adafruit_MotorHAT.FORWARD);
        myMotor4.run(Adafruit_MotorHAT.FORWARD);
        myMotor5.run(Adafruit_MotorHAT.FORWARD);
        myMotor6.run(Adafruit_MotorHAT.FORWARD);
        myMotor7.run(Adafruit_MotorHAT.FORWARD);
        myMotor8.run(Adafruit_MotorHAT.FORWARD);
        
        
	myMotor1.setSpeed(70)
        myMotor2.setSpeed(70)
        myMotor3.setSpeed(70)
        myMotor4.setSpeed(70)
        myMotor5.setSpeed(70)
        myMotor6.setSpeed(70)
        myMotor7.setSpeed(70)
        myMotor8.setSpeed(70)
        time.sleep(0.05)

	
def moveBackward():
        print "Move Backward"
        myMotor1.run(Adafruit_MotorHAT.BACKWARD)
	myMotor2.run(Adafruit_MotorHAT.BACKWARD)
	myMotor3.run(Adafruit_MotorHAT.BACKWARD)
	myMotor4.run(Adafruit_MotorHAT.BACKWARD)
	myMotor5.run(Adafruit_MotorHAT.BACKWARD)
	myMotor6.run(Adafruit_MotorHAT.BACKWARD)
	myMotor7.run(Adafruit_MotorHAT.BACKWARD)
	myMotor8.run(Adafruit_MotorHAT.BACKWARD)
	
        
	myMotor1.setSpeed(100)
        myMotor2.setSpeed(100)
        myMotor3.setSpeed(100)
        myMotor4.setSpeed(100)
        myMotor5.setSpeed(100)
        myMotor6.setSpeed(100)
        myMotor7.setSpeed(100)
        myMotor8.setSpeed(100)
	time.sleep(0.25)

	
	
def turnRight():
        print "Turn Right"
        myMotor1.run(Adafruit_MotorHAT.RELEASE)
        myMotor2.run(Adafruit_MotorHAT.RELEASE)
        myMotor3.run(Adafruit_MotorHAT.RELEASE)
	myMotor4.run(Adafruit_MotorHAT.FORWARD)
	myMotor5.run(Adafruit_MotorHAT.RELEASE)
	myMotor6.run(Adafruit_MotorHAT.RELEASE)
 	 
        
	myMotor1.setSpeed(100)
        myMotor2.setSpeed(100)
        myMotor3.setSpeed(100)
        myMotor4.setSpeed(100)
        myMotor5.setSpeed(100)
        myMotor6.setSpeed(100)
        time.sleep(0.25)

	
        	
def turnLeft():
        print "Turn Left"
        myMotor1.run(Adafruit_MotorHAT.RELEASE)
        myMotor2.run(Adafruit_MotorHAT.RELEASE)
        myMotor3.run(Adafruit_MotorHAT.FORWARD)
	myMotor4.run(Adafruit_MotorHAT.FORWARD)
	myMotor5.run(Adafruit_MotorHAT.RELEASE)
	myMotor6.run(Adafruit_MotorHAT.FORWARD)
	
        
	myMotor1.setSpeed(100)
        myMotor2.setSpeed(100)
        myMotor3.setSpeed(100)
        myMotor4.setSpeed(100)
        myMotor5.setSpeed(100)
        myMotor6.setSpeed(100)
        
        time.sleep(0.25)

	
	myMotor1.setSpeed(100)
	myMotor2.setSpeed(100)
	myMotor3.setSpeed(100)
	myMotor4.setSpeed(100)
	myMotor5.setSpeed(100)
	myMotor6.setSpeed(100)
	time.sleep(0.25)  
        	
def spinRight():
        print "Spin Right"
        myMotor1.run(Adafruit_MotorHAT.BACKWARD)
        myMotor2.run(Adafruit_MotorHAT.BACKWARD)
        myMotor3.run(Adafruit_MotorHAT.BACKWARD)
	myMotor4.run(Adafruit_MotorHAT.FORWARD)
	myMotor5.run(Adafruit_MotorHAT.FORWARD)
	myMotor6.run(Adafruit_MotorHAT.FORWARD)
	
	myMotor1.setSpeed(100)
        myMotor2.setSpeed(100)
        myMotor3.setSpeed(100)
        myMotor4.setSpeed(100)
        myMotor5.setSpeed(100)
        myMotor6.setSpeed(100)
        time.sleep(0.25)

	
def spinLeft():
        print "Spin Left"
        myMotor1.run(Adafruit_MotorHAT.BACKWARD)
        myMotor2.run(Adafruit_MotorHAT.BACKWARD)
        myMotor3.run(Adafruit_MotorHAT.FORWARD)
	myMotor4.run(Adafruit_MotorHAT.FORWARD)
	myMotor5.run(Adafruit_MotorHAT.BACKWARD)
	myMotor6.run(Adafruit_MotorHAT.FORWARD)
	
	
	myMotor1.setSpeed(70)
        myMotor2.setSpeed(70)
        myMotor3.setSpeed(70)
        myMotor4.setSpeed(70)
        myMotor5.setSpeed(70)
        myMotor6.setSpeed(70)
        time.sleep(0.05)

	
        
        
def allStop():
        print "Stop"
        myMotor1.run(Adafruit_MotorHAT.RELEASE);
        myMotor2.run(Adafruit_MotorHAT.RELEASE);
        myMotor3.run(Adafruit_MotorHAT.RELEASE);
        myMotor4.run(Adafruit_MotorHAT.RELEASE);
        myMotor5.run(Adafruit_MotorHAT.RELEASE);
        myMotor6.run(Adafruit_MotorHAT.RELEASE);
        time.sleep(0.25)

try:

  while True:
          
    dis = mr()
    print "Distance : %.1f" % dis
    time.sleep(.15)

    if dis >= 50:
     moveForward()       
    else:
     spinLeft()

except KeyboardInterrupt:

      gpio.cleanup      

#moveForward()
#allStop()
#moveBackward()
#allStop()
#turnRight()
#allStop()
#turnLeft()
#allStop
#spinRight()
#allStop()
#spinLeft()
#allStop()

	
        
        

	
