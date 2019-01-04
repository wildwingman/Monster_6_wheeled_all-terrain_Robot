#!/usr/bin/python


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

gpio.setup(27, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(10, gpio.OUT)
gpio.setup(9, gpio.OUT)

gpio.setup(6, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(19, gpio.OUT)
gpio.setup(26, gpio.OUT)

def forward():
        gpio.output(12, 1)
        gpio.output(16, 0)
        gpio.output(20, 1)
        gpio.output(21, 0)
        
        gpio.output(27, 1)
        gpio.output(22, 0)
        gpio.output(10, 1)
        gpio.output(9, 0)

        gpio.output(6, 1)
        gpio.output(13, 0)
        gpio.output(19, 1)
        gpio.output(26, 0)
def reverse():
        gpio.output(12, 0)
        gpio.output(16, 1)
        gpio.output(20, 0)
        gpio.output(21, 1)
        
        gpio.output(27, 0)
        gpio.output(22, 1)
        gpio.output(10, 0)
        gpio.output(9, 1)

        gpio.output(6, 0)
        gpio.output(13, 1)
        gpio.output(19, 0)
        gpio.output(26, 1)
def turnRight():
        gpio.output(12, 1)
        gpio.output(16, 0)
        gpio.output(20, 0)
        gpio.output(21, 0)
        
        gpio.output(27, 1)
        gpio.output(22, 0)
        gpio.output(10, 0)
        gpio.output(9, 0)

        gpio.output(6, 1)
        gpio.output(13, 0)
        gpio.output(19, 0)
        gpio.output(26, 0)
def turnLeft():
        gpio.output(12, 1)
        gpio.output(16, 1)
        gpio.output(20, 1)
        gpio.output(21, 0)
        
        gpio.output(27, 1)
        gpio.output(22, 1)
        gpio.output(10, 1)
        gpio.output(9, 0)

        gpio.output(6, 1)
        gpio.output(13, 1)
        gpio.output(19, 1)
        gpio.output(26, 0)
def spinRight():
        gpio.output(12, 1)
        gpio.output(16, 0)
        gpio.output(20, 0)
        gpio.output(21, 1)
        
        gpio.output(27, 1)
        gpio.output(22, 0)
        gpio.output(10, 0)
        gpio.output(9, 1)

        gpio.output(6, 1)
        gpio.output(13, 0)
        gpio.output(19, 0)
        gpio.output(26, 1)
def spinLeft():
        gpio.output(12, 0)
        gpio.output(16, 1)
        gpio.output(20, 1)
        gpio.output(21, 0)
        
        gpio.output(27, 0)
        gpio.output(22, 1)
        gpio.output(10, 1)
        gpio.output(9, 0)

        gpio.output(6, 0)
        gpio.output(13, 1)
        gpio.output(19, 1)
        gpio.output(26, 0)

def allStop():
        gpio.output(12, 0)
        gpio.output(16, 0)
        gpio.output(20, 0)
        gpio.output(21, 0)
        
        gpio.output(27, 0)
        gpio.output(22, 0)
        gpio.output(10, 0)
        gpio.output(9, 0)

        gpio.output(6, 0)
        gpio.output(13, 0)
        gpio.output(19, 0)
        gpio.output(26, 0)


        



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


        
