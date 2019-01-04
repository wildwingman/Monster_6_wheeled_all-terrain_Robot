#!/usr/bin/python

# Monster_6wd_obsticle_avoidance_robot_L298N_3_sensor
# External module imports

import RPi.GPIO as GPIO
import time

# Define GPIO For Driver motors
GPIO.setwarnings(False)

GPIO.setmode(gpio.BCM)
GPIO.setup(23, gpio.OUT)
GPIO.setup(24, gpio.IN)

GPIO.setup(12, gpio.OUT)
GPIO.setup(16, gpio.OUT)
GPIO.setup(20, gpio.OUT)
GPIO.setup(21, gpio.OUT)

GPIO.setup(27, gpio.OUT)
GPIO.setup(22, gpio.OUT)
GPIO.setup(10, gpio.OUT)
GPIO.setup(9, gpio.OUT)

GPIO.setup(6, gpio.OUT)
GPIO.setup(13, gpio.OUT)
GPIO.setup(19, gpio.OUT)
GPIO.setup(26, gpio.OUT)

# Define GPIO for ultrasonic central
GPIO_TRIGGER_CENTRAL = 23
GPIO_ECHO_CENTRAL = 24
GPIO.setup(GPIO_TRIGGER_CENTRAL, GPIO.OUT)  # Trigger > Out
GPIO.setup(GPIO_ECHO_CENTRAL, GPIO.IN)      # Echo < In


# Functions for driving
def forward():
        print "Forward"
        
        GPIO.output(27, 1)
        GPIO.output(22, 0)
        GPIO.output(10, 1)
        GPIO.output(9, 0)

def reverse():
        print "Reverse"

        GPIO.output(27, 0)
        GPIO.output(22, 1)
        GPIO.output(10, 0)
        GPIO.output(9, 1)

def turnRight():
        print "Turn Right"
        
        GPIO.output(27, 1)
        GPIO.output(22, 0)
        GPIO.output(10, 0)
        GPIO.output(9, 0)

def turnLeft():
        print "Turn Left"
        
        GPIO.output(27, 1)
        GPIO.output(22, 1)
        GPIO.output(10, 1)
        GPIO.output(9, 0)

def spinRight():
        print "Spin Right"
      
        GPIO.output(27, 1)
        GPIO.output(22, 0)
        GPIO.output(10, 0)
        GPIO.output(9, 1)

def spinLeft():
        print "Spin Left"
       
        GPIO.output(27, 0)
        GPIO.output(22, 1)
        GPIO.output(10, 1)
        GPIO.output(9, 0)

def allStop():
        print "Stop"
        
        GPIO.output(27, 0)
        GPIO.output(22, 0)
        GPIO.output(10, 0)
        GPIO.output(9, 0)

################################# DC motor tees

def frontObstacle():

    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER_CENTRAL, False)
    # Allow module to settle
    time.sleep(0.2)
    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER_CENTRAL, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_CENTRAL, False)
    start = time.time()
    while GPIO.input(GPIO_ECHO_CENTRAL) == 0:
        start = time.time()
    while GPIO.input(GPIO_ECHO_CENTRAL) == 1:
        stop = time.time()
    # Calculate pulse length
    elapsed = stop - start
    # Distance pulse travelled in that time is time
    # Multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000 / 2  # distance of both directions so divide by 2
    print "Front Distance : %.1f" % distance
    return distance

def rightObstacle():
    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER_RIGHT, False)
    # Allow module to settle
    time.sleep(0.2)
    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER_RIGHT, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_RIGHT, False)
    start = time.time()
    while GPIO.input(GPIO_ECHO_RIGHT) == 0:
        start = time.time()
    while GPIO.input(GPIO_ECHO_RIGHT) == 1:
        stop = time.time()
    # Calculate pulse length
    elapsed = stop - start
    # Distance pulse travelled in that time is time
    # Multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000 / 2  # Distance of both directions so divide by 2
    print "Right Distance : %.1f" % distance
    return distance


def leftObstacle():

    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER_LEFT, False)
    # Allow module to settle
    time.sleep(0.2)
    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER_LEFT, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_LEFT, False)
    start = time.time()
    while GPIO.input(GPIO_ECHO_LEFT) == 0:
        start = time.time()
    while GPIO.input(GPIO_ECHO_LEFT) == 1:
        stop = time.time()
    # Calculate pulse length
    elapsed = stop - start
    # Distance pulse travelled in that time is time
    # Multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000 / 2  # Distance of both directions so divide by 2
    print "Left Distance : %.1f" % distance
    return distance


# Check front obstacle and turn right if there is an obstacle
def lookDriveForward():
    while frontObstacle() < 30:
        allStop()
        turnRight()
    forward()



# Avoid obstacles and drive forward
def obDrive():
    forward()
    start = time.time()
    # Drive 5 minutes
    while start > time.time() - 300:  # 300 = 60 seconds * 5
        if frontObstacle() < 30:
            allStop()
            lookDrivefFront()
        elif rightObstacle() < 30:
            allStop() 
            lookDriveRight()
        elif leftObstacle() < 30:
            allStop()
            lookDriveLeft()
    # Clear GPIOs, it will stop motors       
    clearGpios()


def clearGpios():
    print "clearing GPIO"
    GPIO.output(37, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(16, False)
    GPIO.output(33, False)
    GPIO.output(38, False)    
    print "All GPIOs CLEARED"


def main():
    # First clear GPIOs
    cleargpios()
    print "start driving: "
    # Start obstacle avoid driving
    obstacleavoiddrive()

if __name__ == "__main__":
    main()

