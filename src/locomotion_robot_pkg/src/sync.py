#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64

# Initialize encoder counters
encoder_a_count = 0
encoder_b_count = 0
pub = None

# Initialize flags
count_a_received = False
count_b_received = False

# Time between encoder readings
TIME_BETWEEN_READINGS = 0.1

def sync_motors():
    """""Sync motors."""""
    global encoder_a_count, encoder_b_count, count_a_received, count_b_received

    # Calculate difference between encoder counts
    difference = encoder_a_count - encoder_b_count

    print(f'Encoder difference: {difference}')

    count_a_received = False
    count_b_received = False


def get_encoder_count_a(data):
    """""Get encoder count from A."""""
    global encoder_a_count, count_a_received

    encoder_a_count = int(data.data)
    count_a_received = True
    print(encoder_a_count)

    if count_b_received:
        sync_motors()

    return encoder_a_count

def get_encoder_count_b(data):
    """""Get encoder count from B."""""
    global encoder_b_count, count_b_received

    encoder_b_count = int(data.data)
    count_b_received = True
    print(encoder_b_count)

    if count_a_received:
        sync_motors()

    return encoder_b_count


if __name__ == '__main__':
    # Create subscribers
    rospy.Subscriber('encoder_count_a', Int64, get_encoder_count_a)
    rospy.Subscriber('encoder_count_b', Int64, get_encoder_count_b)

    # Create publishers
    # pub = rospy.Publisher("ready_b", Bool, queue_size=10)

    # Initialize node
    rospy.init_node('sync')

    rospy.spin()
