#!/usr/bin/env python3
import sys
import rospy
import time
from locomotion_robot_pkg.msg import sub_move  # Importing custom message type
from std_msgs.msg import Empty

_continue = False  # Flag to indicate whether to continue to the next primitive
start_time = None  # Variable to hold the start time of the movement
end_time = None  # Variable to hold the end time of the movement
pub_sub_move = None  # Publisher object to publish movement commands

# Define commands for different shapes and movements
commands = {
    "test": [("forward", "arg"), ("reverse", "arg"), ("left", "90"), ("right", "90")],
    "line": [("forward", "arg")],
    "square": [("forward", "arg"), ("left", "90"), ("forward", "arg"), ("left", "90"),
                ("forward", "arg"), ("left", "90"), ("forward", "arg"), ("left", "90")]
}

# Functions to execute different movement primitives
def forward(distance):
    # Create a message for moving forward
    forward_sm = sub_move()
    forward_sm.primitive.data = "forward"
    forward_sm.distance.data = distance
    forward_sm.angle.data = 0
    pub_sub_move.publish(forward_sm)

def reverse(distance):
    # Create a message for moving reverse
    reverse_sm = sub_move()
    reverse_sm.primitive.data = "reverse"
    reverse_sm.distance.data = distance
    reverse_sm.angle.data = 0
    pub_sub_move.publish(reverse_sm)

def left(angle):
    # Create a message for turning left
    left_sm = sub_move()
    left_sm.primitive.data = "left"
    left_sm.distance.data = 0
    left_sm.angle.data = angle
    pub_sub_move.publish(left_sm)

def right(angle):
    # Create a message for turning right
    right_sm = sub_move()
    right_sm.primitive.data = "right"
    right_sm.distance.data = 0
    right_sm.angle.data = angle
    pub_sub_move.publish(right_sm)

# Function to send acknowledgment before the first primitive execution
def send_ack():
    ack = sub_move()
    ack.primitive.data = "ack"
    ack.distance.data = 0
    ack.angle.data = 0
    pub_sub_move.publish(ack)

# Callback function triggered when the next primitive needs to be executed
def next_primitive(data):
    global _continue
    print("Next primitive!")
    _continue = True

# Function to decode and execute the command and argument received
def decoder(command, argument):
    global _continue, pub_sub_move, start_time, end_time

    start_time = time.time()

    try:
        primitives_list = commands[command]  # Retrieve the list of primitives for the given command
    except:
        print(f"Command {command} does not exist")
        return

    send_ack()  # Send acknowledgment before starting the movement

    for primitive in primitives_list:
        func_name = primitive[0]
        func_arg = int(primitive[1]) if primitive[1] != "arg" else int(argument)
        
        if func_name in globals() and callable(globals()[func_name]):
            func_to_call = globals()[func_name]
            func_to_call(func_arg)  # Execute the movement primitive
            print("Primitive sent")
        else:
            print(f"Function '{func_name}' not found or not callable.")
            return
   
        _continue = False
        while not _continue:
            pass  # Wait for acknowledgment before moving to the next primitive

    end_time = time.time()
    time_taken = "{:.3f}".format(end_time - start_time)
    rospy.loginfo(f"Finish at: {time_taken}")  # Log the time taken to complete the movement

if __name__ == "__main__":
    pub_sub_move = rospy.Publisher("sub_move", sub_move, queue_size=10)  # Initialize the publisher
    rospy.Subscriber("next_sm", Empty, next_primitive)  # Subscribe to the "next_sm" topic
    rospy.init_node('locomotion')  # Initialize the ROS node

    decoder(sys.argv[1], sys.argv[2])  # Decode and execute the provided command and argument
