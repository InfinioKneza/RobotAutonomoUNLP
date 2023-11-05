#!/usr/bin/env python3
import sys
import rospy
import math
import RPi.GPIO as GPIO
from std_msgs.msg import Int64, Bool, Empty
from locomotion_robot_pkg.msg import sub_move

go_to_next_sm = False
SPEED = 50
WHEEL_DIAMETER = 13.5
ROBOT_DIAMETER = 27
encoder_a_confirmation = False
encoder_b_confirmation = False

## Functions ##
def calculate_pulses_by_distance(distance):
    return int((float(distance) * 2200) / (math.pi * WHEEL_DIAMETER))

def calculate_pulses_by_angle(angle):
    distance = (ROBOT_DIAMETER * math.pi) * angle/360
    return calculate_pulses_by_distance(distance)

def forward(args):
    global SPEED, pub_pulses_to_a, pub_pulses_to_b

    pulses = calculate_pulses_by_distance(args[0])

    pub_pulses_to_a.publish(pulses)
    pub_pulses_to_b.publish(pulses)

    runMotor(0, SPEED, 0)
    runMotor(1, SPEED, 0)

def reverse(args):
    global SPEED, pub_pulses_to_a, pub_pulses_to_b

    pulses = calculate_pulses_by_distance(args[0])

    pub_pulses_to_a.publish(-pulses)
    pub_pulses_to_b.publish(-pulses)

    runMotor(0, SPEED, 1)
    runMotor(1, SPEED, 1)

def left(args):
    global SPEED, pub_pulses_to_a, pub_pulses_to_b

    pulses = calculate_pulses_by_angle(args[1])

    pub_pulses_to_a.publish(pulses)
    pub_pulses_to_b.publish(-pulses)

    runMotor(0, SPEED, 0)
    runMotor(1, SPEED, 1)

def right(args):
    global SPEED, pub_pulses_to_a, pub_pulses_to_b

    pulses = calculate_pulses_by_angle(args[1])

    pub_pulses_to_a.publish(-pulses)
    pub_pulses_to_b.publish(pulses)

    runMotor(0, SPEED, 1)
    runMotor(1, SPEED, 0)

def motorStop():
    GPIO.output(22, GPIO.LOW)

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
        pwma.start(spd)
    elif(motor == 1):
        GPIO.output(15, in1)
        GPIO.output(13, in2)
        pwmb.start(spd)
    
def check_confirmations():
    global encoder_a_confirmation, encoder_b_confirmation

    return encoder_a_confirmation and encoder_b_confirmation


def conf_encoder_a(data):
    global go_to_next_sm, encoder_a_confirmation, encoder_b_confirmation

    encoder_a_confirmation = True
    go_to_next_sm = check_confirmations()

    if go_to_next_sm:
        next_primitive()

def conf_encoder_b(data):
    global go_to_next_sm, encoder_a_confirmation, encoder_b_confirmation
    
    encoder_b_confirmation = True
    go_to_next_sm = check_confirmations()

    if go_to_next_sm:
        next_primitive()

def next_primitive():
    global encoder_a_confirmation, encoder_b_confirmation, pub_next

    encoder_a_confirmation = False
    encoder_b_confirmation = False
    motorStop()
    pub_next.publish()


def receive_primitive(move):
    sub_move = str(move.primitive.data)
    arguments = [int(move.distance.data), int(move.angle.data)]

    print("Sub move: " + sub_move)

    if sub_move == "ack":
        return
    else:
        if sub_move in globals() and callable(globals()[sub_move]):
            func_to_call = globals()[sub_move]
            func_to_call(arguments)


if __name__ == "__main__":
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

    pub_pulses_to_a = rospy.Publisher("wait_pulses_a", Int64, queue_size=10)
    pub_pulses_to_b = rospy.Publisher("wait_pulses_b", Int64, queue_size=10)
    pub_next = rospy.Publisher("next_sm", Empty, queue_size=10)
    rospy.Subscriber("ready_a", Bool, conf_encoder_a)
    rospy.Subscriber("ready_b", Bool, conf_encoder_b)
    rospy.Subscriber("sub_move", sub_move, receive_primitive)
    rospy.init_node('mov')

    rospy.spin()

