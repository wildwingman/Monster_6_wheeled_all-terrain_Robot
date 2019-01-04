#!/usr/bin/python

# Monster_6_Wheeled_all_terrain_Robot_L298N

import RPi.GPIO as gpio
import time
import atexit
import sys
import Tkinter as tk
import pygame
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)



gpio.setup(27, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(10, gpio.OUT)
gpio.setup(9, gpio.OUT)



def forward():
        
        
        gpio.output(27, 1)
        gpio.output(22, 0)
        gpio.output(10, 1)
        gpio.output(9, 0)

        
def reverse():
        
        
        gpio.output(27, 0)
        gpio.output(22, 1)
        gpio.output(10, 0)
        gpio.output(9, 1)

        
def turnLeft():
        
        
        gpio.output(27, 1)
        gpio.output(22, 0)
        gpio.output(10, 0)
        gpio.output(9, 0)

        
def turnRight():
        
        
        gpio.output(27, 1)
        gpio.output(22, 1)
        gpio.output(10, 1)
        gpio.output(9, 0)

        
def spinLeft():
        
        
        gpio.output(27, 1)
        gpio.output(22, 0)
        gpio.output(10, 0)
        gpio.output(9, 1)

        
def spinRight():
        
        
        gpio.output(27, 0)
        gpio.output(22, 1)
        gpio.output(10, 1)
        gpio.output(9, 0)

        

def allStop():
        
        gpio.output(27, 0)
        gpio.output(22, 0)
        gpio.output(10, 0)
        gpio.output(9, 0)

        


        



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
            
try:
	print 'Program running- use your keyboard as a controller'
	while True:
		funcPygameKey(pygame.event.get())

 		time.sleep(0.05)


except KeyboardInterrupt:

	print 'you choose to exit out of the keyboard controller'


        
