#!/usr/bin/env python3
# license removed for brevity
import sys
import rospy
from time import sleep      # Import sleep from time
import RPi.GPIO as GPIO     # Import Standard GPIO Module
from std_msgs.msg import UInt64, Bool

GPIO.setmode(GPIO.BOARD)      # Set GPIO mode to BCM
GPIO.setwarnings(False)

# PWM Frequency
pwmFreq = 100

# Setup Pins for motor controller
GPIO.setup(12, GPIO.OUT)    # PWMA
GPIO.setup(18, GPIO.OUT)    # AIN2
GPIO.setup(16, GPIO.OUT)    # AIN1
GPIO.setup(22, GPIO.OUT)    # STBY
GPIO.setup(15, GPIO.OUT)    # BIN1
GPIO.setup(13, GPIO.OUT)    # BIN2
GPIO.setup(11, GPIO.OUT)    # PWMB

pwma = GPIO.PWM(12, pwmFreq)    # pin 18 to PWM  
pwmb = GPIO.PWM(11, pwmFreq)    # pin 13 to PWM
pwma.start(100)
pwmb.start(100)

_continue = True

## Functions
###############################################################################
def forward(spd):
    runMotor(0, spd, 0)
    runMotor(1, spd, 0)
   

def reverse(spd):
    runMotor(0, spd, 1)
    runMotor(1, spd, 1)
    

def turnLeft(spd):
    runMotor(0, spd, 0)
    runMotor(1, spd, 1)

def turnRight(spd):
    runMotor(0, spd, 1)
    runMotor(1, spd, 0)

def runMotor(motor, spd, direction):
    GPIO.output(22, GPIO.HIGH)
    in1 = GPIO.HIGH
    in2 = GPIO.LOW

    if(direction == 1):
        in1 = GPIO.LOW
        in2 = GPIO.HIGH

    if(motor == 0):
        GPIO.output(16, in1)
        GPIO.output(18, in2)
        pwma.ChangeDutyCycle(spd)
    elif(motor == 1):
        GPIO.output(15, in1)
        GPIO.output(13, in2)
        pwmb.ChangeDutyCycle(spd)
    

def motorStop():
    GPIO.output(22, GPIO.LOW)


def next_move(data):
    global _continue

    rospy.loginfo("Listo movimiento")
    _continue = False
    motorStop()

## Main
##############################################################################
def main(param):
    global _continue

    pub = rospy.Publisher("wait_pulses_b", UInt64, queue_size=10)
    rospy.Subscriber("ready_b", Bool, next_move)
    rospy.init_node('mov')

    distance = int(param)

    pub.publish(distance)
    print("empiezo")

    forward(10)

    while True:
        if not _continue:
            motorStop()    

    rospy.spin()
    """
    while True:
        if (param == 'forward' or param == 'both'):
            forward(100)     # run motor forward
            sleep(2)        # ... for 2 seconds
            motorStop()     # ... stop motor
            sleep(.2)      # delay between motor runs

        if (param == 'reverse' or param == 'both'):
            reverse(100)     # run motor in reverse
            sleep(2)        # ... for 2 seoconds
            motorStop()     # ... stop motor
            sleep(.2)      # delay between motor runs

        if (param == 'stop'):
            motorStop()      # delay between motor runs
        
        
        turnLeft(50)    # turn Left
        sleep(2)        # ... for 2 seconds
        motorStop()     # ... stop motors
        sleep(.25)      # delay between motor runs
        
        turnRight(50)   # turn Right
        sleep(2)        # ... for 2 seconds
        motorStop()     # ... stop motors
        sleep(2)        # delay between motor runs
        """

if __name__ == "__main__":
    #print(sys.argv)
    param = sys.argv[1]
    main(param)

