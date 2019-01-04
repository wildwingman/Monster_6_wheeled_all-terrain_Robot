#!/usr/bin/python

# Monster_4wd_obsticle_avoidance_robot_L298N


import RPi.GPIO as gpio
import time

import atexit
import sys
import Tkinter as tk

gpio.setwarnings(False)

gpio.setmode(gpio.BCM)########## GPIO Pin Numbering



################################ Ultrasonic Sensor Pin Out
gpio.setup(23, gpio.OUT)######## TRIG
gpio.setup(24, gpio.IN)######### ECHO

################################ DC Motor Pin Out
gpio.setup(27, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(10, gpio.OUT)
gpio.setup(9, gpio.OUT)


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

################################ DC motor Direction



def forward():
        print "Forward"
       
        gpio.output(27, 1)
        gpio.output(22, 0)
        gpio.output(10, 1)
        gpio.output(9, 0)
	
def reverse():
        print "Reverse"

        gpio.output(27, 0)
        gpio.output(22, 1)
        gpio.output(10, 0)
        gpio.output(9, 1)
	
def turnRight():
        print "Turn Right"
        
        gpio.output(27, 1)
        gpio.output(22, 0)
        gpio.output(10, 0)
        gpio.output(9, 0)
        	
def turnLeft():
        print "Turn Left"
        
        gpio.output(27, 1)
        gpio.output(22, 1)
        gpio.output(10, 1)
        gpio.output(9, 0)
      
def spinRight():
        print "Spin Right"
        
        gpio.output(27, 1)
        gpio.output(22, 0)
        gpio.output(10, 0)
        gpio.output(9, 1)
	
def spinLeft():
        print "Spin Left"
       
        gpio.output(27, 0)
        gpio.output(22, 1)
        gpio.output(10, 1)
        gpio.output(9, 0)

def allStop():
        print "Stop"

        gpio.output(27, 0)
        gpio.output(22, 0)
        gpio.output(10, 0)
        gpio.output(9, 0)

        

try:

  while True:
          
    dis = mr()
    print "Distance : %.1f" % dis
    time.sleep(.15)

    if dis >= 50:
     forward()       
    else:
     reverse()
     time.sleep(1.5)
     turnLeft()
     time.sleep(1.5)
     

except KeyboardInterrupt:

      gpio.cleanup      


	
        
        

	
