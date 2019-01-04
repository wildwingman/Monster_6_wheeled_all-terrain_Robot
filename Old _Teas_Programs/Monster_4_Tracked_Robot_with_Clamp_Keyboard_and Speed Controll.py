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

gpio.setup(21, gpio.OUT)
gpio.setup(20, gpio.OUT)
gpio.setup(12, gpio.OUT)
gpio.setup(16, gpio.OUT)

def clampOpen():
        gpio.output(21, 1)
        gpio.output(20, 0)

def clampClose():
        gpio.output(21, 0)
        gpio.output(20, 1)

def armUp():
        gpio.output(12, 0)
        gpio.output(16, 1)

def armDown():
        gpio.output(12, 1)
        gpio.output(16, 0)

def allStop():
        gpio.output(21, 0)
        gpio.output(20, 0)
        gpio.output(12, 0)
        gpio.output(16, 0)

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)


#motor pin setup on the Adafruit DC motor Pi Hat
myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(2)
myMotor3 = mh.getMotor(3)
myMotor4 = mh.getMotor(4)
interval = 0.1 #interval to check for key press/release - change to increase/decrease sensetivity
minSpeed = 100 # change this value if you want to reduce the speed of your Truck/Car further. Here 0 will put the motor off.
maxSpeed = 255 # value for Max speed. Here 255 is the Maximum
speed = 255 #Default speed for the back motor
# set the speed to start, from 0 (off) to 255 (max speed)



# set the speed to start, from 0 (off) to 255 (max speed)
#myMotor1.setSpeed(255)
#myMotor2.setSpeed(255)
#myMotor3.setSpeed(255)
#myMotor4.setSpeed(255)
def moveFoward(speed,runTime):
        print "Move Forward"
        myMotor1.setSpeed(speed)
        myMotor1.run(Adafruit_MotorHAT.FORWARD);
        myMotor2.setSpeed(speed)
        myMotor2.run(Adafruit_MotorHAT.FORWARD);
        myMotor3.setSpeed(speed)
        myMotor3.run(Adafruit_MotorHAT.FORWARD);
        myMotor4.setSpeed(speed)
        myMotor4.run(Adafruit_MotorHAT.FORWARD); 
        return;

#moving backward
def moveBackward(speed,runTime):
        print "Move Backward"
        myMotor1.setSpeed(speed)
        myMotor2.setSpeed(speed)
        myMotor3.setSpeed(speed)
        myMotor4.setSpeed(speed)
        myMotor1.run(Adafruit_MotorHAT.BACKWARD)
	myMotor2.run(Adafruit_MotorHAT.BACKWARD)
	myMotor3.run(Adafruit_MotorHAT.BACKWARD)
	myMotor4.run(Adafruit_MotorHAT.BACKWARD)
	return;

#Turn Right
def turnRight(speed,runTime):
        print "Turn Right"
        myMotor1.setSpeed(speed)
        myMotor2.setSpeed(speed)
        myMotor3.setSpeed(speed)
        myMotor4.setSpeed(speed)
        myMotor1.run(Adafruit_MotorHAT.FORWARD)
	myMotor2.run(Adafruit_MotorHAT.FORWARD)
 	myMotor3.run(Adafruit_MotorHAT.RELEASE)
	myMotor4.run(Adafruit_MotorHAT.RELEASE)
	
	return;

#Turn left
def turnLeft(speed,runTime):
        print "Turn Left"
        
        myMotor1.setSpeed(speed)
        myMotor2.setSpeed(speed)
        myMotor3.setSpeed(speed)
        myMotor4.setSpeed(speed)
        myMotor1.run(Adafruit_MotorHAT.RELEASE)
	myMotor2.run(Adafruit_MotorHAT.RELEASE)
	myMotor3.run(Adafruit_MotorHAT.FORWARD)
	myMotor4.run(Adafruit_MotorHAT.FORWARD)
	
	return;

#Spin Right
def spinRight(speed,runTime):
        print "Rotate Right"
        myMotor1.setSpeed(speed)
        myMotor2.setSpeed(speed)
        myMotor3.setSpeed(speed)
        myMotor4.setSpeed(speed)
        myMotor1.run(Adafruit_MotorHAT.FORWARD)
	myMotor2.run(Adafruit_MotorHAT.FORWARD)
	myMotor3.run(Adafruit_MotorHAT.BACKWARD)
	myMotor4.run(Adafruit_MotorHAT.BACKWARD) 
	
	return;

#Spin left
def spinLeft(speed,runTime):
        print "Rotate Left"
        myMotor1.setSpeed(speed)
        myMotor2.setSpeed(speed)
        myMotor3.setSpeed(speed)
        myMotor4.setSpeed(speed)
        myMotor1.run(Adafruit_MotorHAT.BACKWARD)
	myMotor2.run(Adafruit_MotorHAT.BACKWARD)
	myMotor3.run(Adafruit_MotorHAT.FORWARD)
	myMotor4.run(Adafruit_MotorHAT.FORWARD)

	return;
	#time.sleep(runTime);
	# turn on motor
	#motorBack.run(Adafruit_MotorHAT.RELEASE);
	#motorFront.run(Adafruit_MotorHAT.RELEAS



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
                print speed
                moveFoward(speed, 0.25)
            elif event.key == pygame.K_s:
                print 'Key s -backward pressed'
                moveBackward(speed, 0.25)
            elif event.key == pygame.K_a:
                print 'Key a -left turn pressed'
                turnLeft(speed, 0.25)
            elif event.key == pygame.K_d:
                print 'Key d -right turn pressed'
                turnRight(speed, 0.25)
            elif event.key == pygame.K_e:
                print 'Key e -Rotate Right pressed'
                spinRight(speed, 0.25)
            elif event.key == pygame.K_q:
                print 'Key q -Rotate Right pressed'
                spinLeft(speed, 0.25)
            elif event.key == pygame.K_z:
                print 'Key z -increase speed pressed'
                if speed <= maxSpeed:
                	speed = speed + 10 #increaseing speed by 10
                	print 'speed +10'
                else:
                	speed = maxSpeed
                	print 'speed else'
            elif event.key == pygame.K_c:
                print 'Key c - slower speed pressed'
                if speed <= minSpeed:
                	speed = minSpeed
                	print 'speed = minSpeed'
                else:
                	speed = speed - 10
                	print 'speed -10'     
            elif event.key == pygame.K_y:
                print 'Key y Arm Up Pressed'
                armUp()
            elif event.key == pygame.K_h:
                print 'Key h Arm Down Pressed'
                armDown()
            elif event.key == pygame.K_t:
                print 'Key t Clamp Open Pressed'
                clampOpen()
            elif event.key == pygame.K_u:
                print 'Key u Close Pressed'
                clampClose()

#Speed Test Code
                
            elif event.key == pygame.K_z:
                print 'Key z -increase speed pressed'
                if speed <= maxSpeed:
                	speed = speed + 10 #increaseing speed by 10
                	print 'speed +10'
                else:
                	speed = maxSpeed
                	print 'speed else'
            elif event.key == pygame.K_c:
                print 'Key c - slower speed pressed'
                if speed <= minSpeed:
                	speed = minSpeed
                	print 'speed = minSpeed'
                else:
                	speed = speed - 10
                	print 'speed -10'
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
                myMotor4.run(Adafruit_MotorHAT.RELEASE)
            elif event.key == pygame.K_y:
                print 'Key y Arm Up Released'
                allStop()
            elif event.key == pygame.K_h:
                print 'Key h Arm Down Released'
                allStop()
            elif event.key == pygame.K_t:
                print 'Key t clamp Open Released'
                allStop()
            elif event.key == pygame.K_u:
                print 'Key u Clamp Close Released'
                allStop()
                
            
#moving foward ..
#moveFoward(speed,0.25)
#time.sleep(0.5);
# turn on motor
myMotor1.run(Adafruit_MotorHAT.RELEASE);
myMotor2.run(Adafruit_MotorHAT.RELEASE);
myMotor3.run(Adafruit_MotorHAT.RELEASE);
myMotor4.run(Adafruit_MotorHAT.RELEASE);

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
