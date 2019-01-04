#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import pygame #for more info on keyboard events -- https://www.pygame.org/docs/ref/key.html
import time
import atexit

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)



def panLeft():
  print "Move Left"
  servo1Max = 600  # Max pulse length out of 4096
  servo1Min = 0  # Max pulse length out of 4096
  return;
def panRight():
  print "Move Rifgt"
  servo1Min = 257  # Max pulse length out of 4096
  return;

def tiltUp():
  print "Move Up"
  servo1Max = 785  # Max pulse length out of 4096 
  return;
def tiltDown():
  print "Move Down"
  servoMin = 220  # Min pulse length out of 4096
  return;

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)
  
pwm.setPWMFreq(60)                        # Set frequency to 60 Hz


  
pygame.init()
screen = pygame.display.set_mode([400,400]) #this seems to work without a montior connected and also when .py is run via SSH
pygame.display.set_caption("Adafruit Servo Hat with Keyboard Control")

def funcPygameKey(events):
    
    global servoMin
    global servoMax
    global servo1Min
    global servo1Max
    for event in events:

        if event.type == pygame.QUIT:
                print 'quite pygame'
        elif event.type == pygame.KEYDOWN:
            # checking if a key is pressed 
            if event.key == pygame.K_i:
                    #print 'Key i -Pan Left Pressed'
                    panLeft()
            elif event.key == pygame.K_p:
                      #print 'Key h -Pan Right pressed'
                      panRight()
            elif event.key == pygame.K_o:
                      #print 'Key s -Tilt Up pressed'
                      tiltUp()
            elif event.key == pygame.K_l:
                      #print 'Key s -Tilt Down pressed'
                      tiltDown()
       
            elif event.type == pygame.KEYUP:
            # checking if a key is released
              if event.key == pygame.K_i:
               print "Key i-Move Left"
               servo1Max = 600  # Max pulse length out of 4096
               return;
              elif event.key == pygame.K_p: 
               print "Key p-Move Right"
               servo1Min = 257  # Max pulse length out of 4096
               return; 
              elif event.key == pygame.K_o:
                print 'Key o -Move Up  released'
                print "Key t-Move Up"
                servo1Max = 785  # Max pulse length out of 4096 
                return; 
              elif event.key == pygame.K_l:
                print "Key l-Move Down"
                servoMin = 220  # Min pulse length out of 4096
                return;  


try:
	print 'Program running- use your keyboard as a controller'
	while True:
		funcPygameKey(pygame.event.get())

 		time.sleep(0.05)


except KeyboardInterrupt:

	print 'you choose to exit out of the keyboard controller'
 
