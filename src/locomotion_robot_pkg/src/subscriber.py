#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import argparse
import RPi.GPIO as GPIO     # Import Standard GPIO Module
from time import sleep      # Import sleep from time



GPIO.setmode(GPIO.BOARD)      # Set GPIO mode to BCM
GPIO.setwarnings(False);

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
    GPIO.output(22, GPIO.HIGH);
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


def roboto(action, param):
    if (param == 'forward' or param == 'both') and (action != 800):
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
        

def callback(data, param):
    action = data.data
    roboto(action, param)
    
def listener(param):

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback, callback_args=(param,))

    # spin() simply keeps python from exiting until this node is stopped
    #rospy.spin()

    # Agrega un bucle para mantener el nodo en ejecución
    while not rospy.is_shutdown():
        rospy.spinOnce()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('param', type=str, help='Specify the action parameter')
    args = parser.parse_args()
    try:
        listener(args.param)
    except rospy.ROSInterruptException:
        pass
