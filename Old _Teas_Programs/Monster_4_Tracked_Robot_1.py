#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import RPi.GPIO as gpio
import time
import atexit
import sys
import Tkinter as tk
import pygame
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

gpio.setup(12, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.OUT)

def forward():
        gpio.output(12, 1)
        gpio.output(16, 0)
        gpio.output(20, 1)
        gpio.output(21, 0)
def reverse():
        gpio.output(12, 0)
        gpio.output(16, 1)
        gpio.output(20, 0)
        gpio.output(21, 1)
def turnRight():
        gpio.output(12, 1)
        gpio.output(16, 0)
        gpio.output(20, 0)
        gpio.output(21, 0)
def turnLeft():
        gpio.output(12, 1)
        gpio.output(16, 1)
        gpio.output(20, 1)
        gpio.output(21, 0)
def spinRight():
        gpio.output(12, 1)
        gpio.output(16, 0)
        gpio.output(20, 0)
        gpio.output(21, 1)
def spinLeft():
        gpio.output(12, 0)
        gpio.output(16, 1)
        gpio.output(20, 1)
        gpio.output(21, 0)

def allStop():
        gpio.output(13, 0)
        gpio.output(15, 0)
        gpio.output(19, 0)
        gpio.output(21, 1)

def allStop():
        gpio.output(12, 0)
        gpio.output(16, 0)
        gpio.output(20, 0)
        gpio.output(21, 0)

# create a default object, no changes to I2C address or frequency
#mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!


#motor pin setup on the Adafruit DC motor Pi Hat


# set the speed to start, from 0 (off) to 255 (max speed)



# set the speed to start, from 0 (off) to 255 (max speed)


        



pygame.init()
screen = pygame.display.set_mode([400,400]) #this seems to work without a montior connected and also when .py is run via SSH
pygame.display.set_caption("Motor Control")

def funcPygameKey(events):
    # Variables accessible outside this function
    global speed
    global maxSpeed
    global minSpeed
    for event in events:
        if event.type == pygame.QUIT:
        	print 'quite pygame'
        elif event.type == pygame.KEYDOWN:
            # checking if a key is pressed
            if event.key == pygame.K_w: #change the mapping if your not comfotable refer to the url for mapping - https://www.pygame.org/docs/ref/key.html
                print 'Key w -forward pressed'
                #print speed
                forward()
            elif event.key == pygame.K_s:
                print 'Key s -reverse pressed'
                reverse()
            elif event.key == pygame.K_a:
                print 'Key a -left turn pressed'
                turnLeft()
            elif event.key == pygame.K_d:
                print 'Key d -right turn pressed'
                turnRight()
            elif event.key == pygame.K_e:
                print 'Key e -Rotate Right pressed'
                spinRight()
            elif event.key == pygame.K_q:
                print 'Key q -Rotate Right pressed'
                spinLeft()
            
            #elif event.key == pygame.K_z:
             #   print 'Key z -increase speed pressed'
              #  if speed <= maxSpeed:
               # 	speed = speed + 10 #increaseing speed by 10
                #	print 'speed +10'
                #else:
                #	speed = maxSpeed
                #	print 'speed else'
            #elif event.key == pygame.K_c:
             #   print 'Key c - slower speed pressed'
              #  if speed <= minSpeed:
               # 	speed = minSpeed
                #	print 'speed = minSpeed'
               # else:
                #	speed = speed - 10
                #	print 'speed -10'
            #elif event.key == pygame.K_r:
             #   print 'Key r -back right pressed'
              #  spinRight(speed,200,0.25)
            #elif event.key == pygame.K_f:
             #   print 'Key f -back left pressed'
              #  spinLeft(speed,200,0.25)
        elif event.type == pygame.KEYUP:
            # checking if a key is released
            if event.key == pygame.K_w:
                print 'Key w -Foward released'
                allStop() 
            elif event.key == pygame.K_s:
                print 'Key s -Backward released'
                allStop()
                
            elif event.key == pygame.K_a:
                print 'Key a -Left Turn released'
                allStop()
            elif event.key == pygame.K_d:
                print 'Key d -Right Turn released'
                allStop()
            elif event.key == pygame.K_q:
                print 'Key q -Rotate Left released'
                allStop()
            elif event.key == pygame.K_e:
                print 'Key e -Rotate Right released'
                allStop()
            
                
            
#moving foward ..
 #moveFoward(speed,0.25)
#time.sleep(0.5);
# turn on motor
#motorBack.run(Adafruit_MotorHAT.RELEASE);

try:
	print 'Program running- use your keyboard as a controller'
	while True:
		funcPygameKey(pygame.event.get())

 		time.sleep(0.05)


except KeyboardInterrupt:

	print 'you choose to exit out of the keyboard controller'


        
