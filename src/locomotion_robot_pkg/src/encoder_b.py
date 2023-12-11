#!/usr/bin/env python3
import time
import rospy
from std_msgs.msg import Int64, Bool
import RPi.GPIO as GPIO

# Configure encoder pins
PIN_ENCODER_B1 = 35
PIN_ENCODER_B2 = 37

# Initialize encoder counter
encoder_count = 0
target = 0  # Target encoder count
counting = False  # Flag to indicate if we are counting
pub_ready = None  # Publisher to send confirmation
pub_encoder_count = None  # Publisher to send encoder count

start_time = 0

# Variable to store the previous state of pin B
last_state_B = None


def callback_encoder_B(channel):
    """""Callback function for encoder B."""""

    global encoder_count, last_state_B, counting, target, start_time, pub_encoder_count

    # Read the current state of pin B1
    state_B1 = GPIO.input(PIN_ENCODER_B1)

    # Read the current state of pin B2
    state_B2 = GPIO.input(PIN_ENCODER_B2)

    if last_state_B is None:
        last_state_B = state_B1
        return
    
    # Check for a change in encoder
    if state_B1 != last_state_B:
        # If pin B2 is in the same state as pin B1, it rotates in one direction
        if state_B2 == state_B1:
            encoder_count -= 1
        else:
            encoder_count += 1

    # Calculate elapsed time
    elapsed_time = time.time() - start_time

    # Publish encoder count when elapsed time is greater than 0.1
    if elapsed_time > 0.1:
        pub_encoder_count.publish(encoder_count)
        start_time = time.time()

    # print("Enc_B: " + str(encoder_count))

    if counting:
        if target >= 0:
            if encoder_count >= target:
                send_ready()
        else:
            if encoder_count <= target:
                send_ready()

    last_state_B = state_B1


def send_ready():
    """""Send ready message to the controller."""""
    global counting, pub_ready

    print("Counted from B!")
    counting = False
    pub_ready.publish(True)


def start_counting_cb(data):
    """""Callback function for start_counting_b."""""
    global encoder_count, counting, target

    print("Starting counting from B")

    target = int(data.data)  # Get target encoder count
    encoder_count = 0  # Resets counter
    counting = True


if __name__ == '__main__':
    # Initialize GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_ENCODER_B1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PIN_ENCODER_B2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Add callback function for encoder B
    GPIO.add_event_detect(PIN_ENCODER_B1, GPIO.BOTH, callback=callback_encoder_B)

    # Initialize node
    rospy.Subscriber('wait_pulses_b', Int64, start_counting_cb)
    pub_ready = rospy.Publisher("ready_b", Bool, queue_size=10)
    pub_encoder_count = rospy.Publisher("encoder_count_b", Int64, queue_size=10)
    rospy.init_node('encoder_b')

    rospy.spin()
