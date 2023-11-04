#!/usr/bin/env python3
import sys
import rospy
import time
import RPi.GPIO as GPIO
from std_msgs.msg import UInt64, Bool
from locomotion_robot_pkg.msg import sub_move

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
start_time = None
end_time = None

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


def next_move_b(data):
    global _continue, start_time, end_time

    end_time = time.time()
    time_taken = "{:.3f}".format(end_time - start_time)
    rospy.loginfo(f"Finish at: {time_taken}")
    
    _continue = False
    motorStop()

def next_move_a(data):
    global _continue, start_time, end_time

    end_time = time.time()
    time_taken = "{:.3f}".format(end_time - start_time)
    rospy.loginfo(f"Finish at: {time_taken}")
    
    _continue = False
    motorStop()

def next_primitive(move):
    print(move)

### Main ###
def main():
    global _continue, start_time

    # pub_pulses_to_a = rospy.Publisher("mlp/wait_pulses_a", UInt64, queue_size=10)
    # pub_pulses_to_b = rospy.Publisher("mlp/wait_pulses_b", UInt64, queue_size=10)
    # rospy.Subscriber("mlp/ready_b", Bool, next_move_b)
    # rospy.Subscriber("mlp/ready_a", Bool, next_move_a)
    rospy.Subscriber("sub_move", sub_move, next_primitive)
    rospy.init_node('mov')

    #pub_pulses_to_b.publish(distance)
    start_time = time.time()

    #forward(50)

    rospy.spin()


if __name__ == "__main__":
    main()

