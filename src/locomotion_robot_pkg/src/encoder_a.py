#!/usr/bin/env python3
import time
import rospy
from std_msgs.msg import Int64, Bool
import RPi.GPIO as GPIO
from constants import SYNC_TIME

# Configure encoder pins
PIN_ENCODER_A1 = 29
PIN_ENCODER_A2 = 31

# Initialize encoder counter
encoder_count = 0
target = 0  # Target encoder count
counting = False  # Flag to indicate if we are counting
pub_ready = None  # Publisher to send confirmation
pub_encoder_count = None  # Publisher to send encoder count

# Variable to store the previous state of pin A
last_state_A = None

start_time = 0

def callback_encoder_A(channel):
    """""Callback function for encoder A."""""

    global encoder_count, last_state_A, counting, target, start_time, pub_encoder_count

    # Read the current state of pin A1
    state_A1 = GPIO.input(PIN_ENCODER_A1)

    # Read the current state of pin A2
    state_A2 = GPIO.input(PIN_ENCODER_A2)

    if last_state_A is None:
        last_state_A = state_A1
        return
    
    # Check for a change in encoder
    if state_A1 != last_state_A:
        # Si el pin B está en el mismo estado que el pin A, gira en un sentido
        if state_A2 == state_A1:
            encoder_count += 1
        else:
            encoder_count -= 1

    # Calculate elapsed time
    elapsed_time = time.time() - start_time

    # Publish encoder count when elapsed time is greater than SYNC_TIME
    if elapsed_time >= SYNC_TIME:
        pub_encoder_count.publish(encoder_count)
        start_time = time.time()

    #print("Enc_A: " + str(encoder_count))

    if counting:
        if target >= 0:
            if encoder_count >= target:
                send_ready()
        else:
            if encoder_count <= target:
                send_ready()

    last_state_A = state_A1

def send_ready():
    global counting, pub_ready

    counting = False
    pub_ready.publish(True)


def start_counting_cb(data):
    """""Callback function for start_counting_a topic."""""
    global encoder_count, counting, target

    target = int(data.data)  # Get target encoder count
    encoder_count = 0  # Resets counter
    counting = True  # Starts counting


if __name__ == '__main__':
    # Initialize GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_ENCODER_A1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PIN_ENCODER_A2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Add callback function for encoder A
    GPIO.add_event_detect(PIN_ENCODER_A1, GPIO.BOTH, callback=callback_encoder_A)

    # Initialize node
    rospy.Subscriber('wait_pulses_a', Int64, start_counting_cb)
    pub_ready = rospy.Publisher("ready_a", Bool, queue_size=10)
    pub_encoder_count = rospy.Publisher("encoder_count_a", Int64, queue_size=10)
    rospy.init_node('encoder_a')
    
    rospy.spin()
