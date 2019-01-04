#!/usr/bin/python
import RPi.GPIO as gpio
import time


gpio.setwarnings(False)
gpio.setmode(gpio.BCM)


gpio.setup(12, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.OUT)

def forward():
    print "forward"
    gpio.output(12, 1)
    gpio.output(16, 0)
    gpio.output(20, 1)
    gpio.output(21, 0)

def reverse():
    print "reverse"
    gpio.output(12, 0)
    gpio.output(16, 1)
    gpio.output(20, 0)
    gpio.output(21, 1)

def turnLeft():
    print "turn left"
    gpio.output(12, 1)
    gpio.output(16, 1)
    gpio.output(20, 1)
    gpio.output(21, 0)

def turnRight():
    print "turn right"
    gpio.output(12, 1)
    gpio.output(16, 0)
    gpio.output(20, 0)
    gpio.output(21, 0)

def spinLeft():
    print "spin left"
    gpio.output(12, 0)
    gpio.output(16, 1)
    gpio.output(20, 1)
    gpio.output(21, 0)

def spinRight():
    print "spin right"
    gpio.output(12, 1)
    gpio.output(16, 0)
    gpio.output(20, 0)
    gpio.output(21, 1)

def allStop():
    print "all stop"
    gpio.output(12, 0)
    gpio.output(16, 0)
    gpio.output(20, 0)
    gpio.output(21, 0)



forward()
time.sleep(3)
reverse()
time.sleep(3)
turnLeft()
time.sleep(3)
turnRight()
time.sleep(3)
spinLeft()
time.sleep(3)
spinRight()
time.sleep(3)
allStop()

gpio.cleanup()


    
