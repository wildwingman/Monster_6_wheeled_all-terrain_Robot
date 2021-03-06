#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import RPi.GPIO as gpio
import time
import atexit
import sys
import Tkinter as tk
import pygame
#gpio.setwarnings(False)

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

atexit.register(turnOffMotors)
#motor pin setup on the Adafruit DC motor Pi Hat
myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(2)
myMotor3 = mh.getMotor(3)
myMotor4 = mh.getMotor(4)

# set the speed to start, from 0 (off) to 255 (max speed)
atexit.register(turnOffMotors)


# set the speed to start, from 0 (off) to 255 (max speed)
myMotor1.setSpeed(255)
myMotor2.setSpeed(255)
myMotor3.setSpeed(255)
myMotor4.setSpeed(255)
def moveFoward():
        print "Move Forward"
        myMotor1.run(Adafruit_MotorHAT.FORWARD);
        myMotor2.run(Adafruit_MotorHAT.FORWARD);
        myMotor3.run(Adafruit_MotorHAT.FORWARD);
        myMotor4.run(Adafruit_MotorHAT.FORWARD); 
        return;

#moving backward
def moveBackward():
        print "Move Backward"
        myMotor1.run(Adafruit_MotorHAT.BACKWARD)
	myMotor2.run(Adafruit_MotorHAT.BACKWARD)
	myMotor3.run(Adafruit_MotorHAT.BACKWARD)
	myMotor4.run(Adafruit_MotorHAT.BACKWARD)
	return;

#Turn Right
def turnRight():
        print "Turn Right"
        myMotor1.run(Adafruit_MotorHAT.FORWARD)
	myMotor2.run(Adafruit_MotorHAT.FORWARD)
 	myMotor3.run(Adafruit_MotorHAT.RELEASE)
	myMotor4.run(Adafruit_MotorHAT.RELEASE)
	
	return;

#Turn left
def turnLeft():
        print "Turn Left"
        myMotor1.run(Adafruit_MotorHAT.RELEASE)
	myMotor2.run(Adafruit_MotorHAT.RELEASE)
	myMotor3.run(Adafruit_MotorHAT.FORWARD)
	myMotor4.run(Adafruit_MotorHAT.FORWARD)
	
	return;

#Spin Right
def spinRight():
        print "Rotate Right"
        myMotor1.run(Adafruit_MotorHAT.FORWARD)
	myMotor2.run(Adafruit_MotorHAT.FORWARD)
	myMotor3.run(Adafruit_MotorHAT.BACKWARD)
	myMotor4.run(Adafruit_MotorHAT.BACKWARD) 
	
	return;

#Spin left
def spinLeft():
        print "Rotate Left"
        myMotor1.run(Adafruit_MotorHAT.BACKWARD)
	myMotor2.run(Adafruit_MotorHAT.BACKWARD)
	myMotor3.run(Adafruit_MotorHAT.FORWARD)
	myMotor4.run(Adafruit_MotorHAT.FORWARD)
	#time.sleep(runTime);
	# turn on motor
	#motorBack.run(Adafruit_MotorHAT.RELEASE);
	#motorFront.run(Adafruit_MotorHAT.RELEASE);
	return;


pygame.init()
screen = pygame.display.set_mode([400,400]) #this seems to work without a montior connected and also when .py is run via SSH
pygame.display.set_caption("Adafruit Mortrol Hat with Keyboard Control")

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
                print 'Key w -foward pressed'
                #print speed
                moveFoward()
            elif event.key == pygame.K_s:
                print 'Key s -backward pressed'
                moveBackward()
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
                print 'Key w-Foward released'
                myMotor1.run(Adafruit_MotorHAT.RELEASE);
                myMotor2.run(Adafruit_MotorHAT.RELEASE);
                myMotor3.run(Adafruit_MotorHAT.RELEASE);
                myMotor4.run(Adafruit_MotorHAT.RELEASE); 
            elif event.key == pygame.K_s:
                print 'Key s-Backward released'
                myMotor1.run(Adafruit_MotorHAT.RELEASE);
                myMotor2.run(Adafruit_MotorHAT.RELEASE);
                myMotor3.run(Adafruit_MotorHAT.RELEASE);
                myMotor4.run(Adafruit_MotorHAT.RELEASE);
                
            elif event.key == pygame.K_a:
                print 'Key a -Left Turn released'
                myMotor1.run(Adafruit_MotorHAT.RELEASE);
                myMotor2.run(Adafruit_MotorHAT.RELEASE);
                myMotor3.run(Adafruit_MotorHAT.RELEASE);
                myMotor4.run(Adafruit_MotorHAT.RELEASE);
            elif event.key == pygame.K_d:
                print 'Key d -Right Turn released'
                myMotor1.run(Adafruit_MotorHAT.RELEASE);
                myMotor2.run(Adafruit_MotorHAT.RELEASE);
                myMotor3.run(Adafruit_MotorHAT.RELEASE);
                myMotor4.run(Adafruit_MotorHAT.RELEASE);
            elif event.key == pygame.K_q:
                print 'Key q -Rotate Left released'
                myMotor1.run(Adafruit_MotorHAT.RELEASE);
                myMotor2.run(Adafruit_MotorHAT.RELEASE);
                myMotor3.run(Adafruit_MotorHAT.RELEASE);
                myMotor4.run(Adafruit_MotorHAT.RELEASE);
            elif event.key == pygame.K_e:
                print 'Key e -Rotate Right released'
                myMotor1.run(Adafruit_MotorHAT.RELEASE);
                myMotor2.run(Adafruit_MotorHAT.RELEASE);
                myMotor3.run(Adafruit_MotorHAT.RELEASE);
                myMotor4.run(Adafruit_MotorHAT.RELEASE);     
            
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


        myMotor1.run(Adafruit_MotorHAT.FORWARD)
	myMotor2.run(Adafruit_MotorHAT.FORWARD)
	myMotor3.run(Adafruit_MotorHAT.RELEASE)
	myMotor4.run(Adafruit_MotorHAT.RELEASE)
