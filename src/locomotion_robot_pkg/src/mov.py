#!/usr/bin/env python3
import rospy
import math
import RPi.GPIO as GPIO
from std_msgs.msg import Int64, Bool, Empty
from locomotion_robot_pkg.msg import sub_move, sync_type, motor_speeds
from constants import ROBOT_DIAMETER, WHEEL_DIAMETER, PULSES_PER_FULL_REVOLUTION, SYNC_ENABLE

# Initialize variables
go_to_next_sm = False # Flag to indicate if we are going to the next submovemnt
motor_a_speed = 50  # Initial speed of motor A
motor_b_speed = 50  # Initial speed of motor B

last_sync_type = -1  # Saves the last sync_type message sent to avoid congestion
encoder_a_confirmation = False
encoder_b_confirmation = False

# Calculate pulses based on distance
def calculate_pulses_by_distance(distance):
    return int((float(distance) * PULSES_PER_FULL_REVOLUTION) / (math.pi * WHEEL_DIAMETER))

# Calculate pulses based on angle
def calculate_pulses_by_angle(angle):
    distance = (ROBOT_DIAMETER * 2*math.pi) * angle/360
    return calculate_pulses_by_distance(distance)

def sync_movement(_sync_type):
    global pub_sync, last_sync_type

    # Only if the sync_type differs is the message sent
    if last_sync_type ==_sync_type:
        return
    
    # If sync_type is 0 in regular syncronization (not weighted), use whith regular primitives (FRLR)
    if _sync_type == 0:
        sync_msg = sync_type()
        sync_msg.sync_type.data = 0
        sync_msg.factor.data = 0
        sync_msg.dominant_motor.data = 0
        pub_sync.publish(sync_msg)
        last_sync_type = _sync_type
    elif _sync_type == 1:
        pass  # When the sync_type is weighted, use for curve movement

# Move functions
def forward(args):
    global pub_pulses_to_a, pub_pulses_to_b, motor_a_speed, motor_b_speed

    pulses = calculate_pulses_by_distance(args[0])

    if SYNC_ENABLE:
        sync_movement(0)
    
    pub_pulses_to_a.publish(pulses)
    pub_pulses_to_b.publish(pulses)

    runMotor(0, motor_a_speed, 0)
    runMotor(1, motor_b_speed, 0)

def reverse(args):
    global pub_pulses_to_a, pub_pulses_to_b, motor_a_speed, motor_b_speed

    pulses = calculate_pulses_by_distance(args[0])

    if SYNC_ENABLE:
        sync_movement(0)

    pub_pulses_to_a.publish(-pulses)  # Negative because we are going backwards
    pub_pulses_to_b.publish(-pulses)

    runMotor(0, motor_a_speed, 1)
    runMotor(1, motor_b_speed, 1)

def left(args):
    global pub_pulses_to_a, pub_pulses_to_b, motor_a_speed, motor_b_speed

    pulses = calculate_pulses_by_angle(args[1])

    if SYNC_ENABLE:
        sync_movement(0)
    
    pub_pulses_to_a.publish(pulses)
    pub_pulses_to_b.publish(-pulses)

    runMotor(0, motor_a_speed, 0)
    runMotor(1, motor_b_speed, 1)

def right(args):
    global pub_pulses_to_a, pub_pulses_to_b, motor_a_speed, motor_b_speed

    pulses = calculate_pulses_by_angle(args[1])

    if SYNC_ENABLE:
        sync_movement(0)
    
    pub_pulses_to_a.publish(-pulses)
    pub_pulses_to_b.publish(pulses)

    runMotor(0, motor_a_speed, 1)
    runMotor(1, motor_b_speed, 0)

# Stop motor function
def motorStop():
    GPIO.output(22, GPIO.LOW)

# Run motor function
def runMotor(motor, spd, direction):
    GPIO.output(22, GPIO.HIGH)
    in1 = GPIO.HIGH
    in2 = GPIO.LOW

    # Reverse direction for going backwards
    if direction == 1:
        in1 = GPIO.LOW
        in2 = GPIO.HIGH

    if motor == 0:
        GPIO.output(16, in1)
        GPIO.output(18, in2)
        pwma.start(spd)
    elif motor == 1:
        GPIO.output(15, in1)
        GPIO.output(13, in2)
        pwmb.start(spd)


def update_speeds_cb(motor_speeds_msg):
    global motor_a_speed, motor_b_speed

    if not SYNC_ENABLE:
        return

    motor_a_speed = float(motor_speeds_msg.vel_a.data)  # Get motor A speed
    motor_b_speed = float(motor_speeds_msg.vel_b.data)  # Get motor B speed

    # Updates motors speed
    pwma.start(motor_a_speed)
    pwmb.start(motor_b_speed)
    print("Speed A: {:.2f}".format(motor_a_speed))
    print("Speed B: {:.2f}".format(motor_b_speed))

# Confirm encoder A
def conf_encoder_a(data):
    global go_to_next_sm, encoder_a_confirmation, encoder_b_confirmation

    encoder_a_confirmation = True

    if encoder_b_confirmation:
        next_primitive()

# Confirm encoder B
def conf_encoder_b(data):
    global go_to_next_sm, encoder_a_confirmation, encoder_b_confirmation

    encoder_b_confirmation = True

    if encoder_a_confirmation:
        next_primitive()

# Move to next primitive
def next_primitive():
    global encoder_a_confirmation, encoder_b_confirmation, pub_next

    encoder_a_confirmation = False
    encoder_b_confirmation = False
    motorStop()
    pub_next.publish()

# Receive primitive to execute
def receive_primitive(move):
    sub_move = str(move.primitive.data)  # Get sub move
    arguments = [int(move.distance.data), int(move.angle.data)]  # Get distance and angle

    print("Sub move: " + sub_move)

    # Check if sub move is valid
    if sub_move == "ack":
        return
    else:
        if sub_move in globals() and callable(globals()[sub_move]):
            func_to_call = globals()[sub_move]
            func_to_call(arguments)

# Initialize GPIO
if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
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

    pwma = GPIO.PWM(12, pwmFreq)  # pin 12 to PWM  
    pwmb = GPIO.PWM(11, pwmFreq)  # pin 11 to PWM

    # ROS Publishers and Subscribers initialization
    pub_pulses_to_a = rospy.Publisher("wait_pulses_a", Int64, queue_size=10)
    pub_pulses_to_b = rospy.Publisher("wait_pulses_b", Int64, queue_size=10)
    pub_next = rospy.Publisher("next_sm", Empty, queue_size=10)
    pub_sync = rospy.Publisher("sync_update", sync_type, queue_size=10)

    # Add subscribers for encoder A and B
    rospy.Subscriber("ready_a", Bool, conf_encoder_a)
    rospy.Subscriber("ready_b", Bool, conf_encoder_b)
    # Add subscriber for sub move
    rospy.Subscriber("sub_move", sub_move, receive_primitive)
    # Add subscriber for
    rospy.Subscriber("speed_update", motor_speeds, update_speeds_cb)

    # Initialize node
    rospy.init_node('mov')

    rospy.spin()