#!/usr/bin/env python3
import sys
import rospy
import time
from locomotion_robot_pkg.msg import sub_move
from std_msgs.msg import Empty

_continue = False
start_time = None
end_time = None
pub_sub_move = None

commands = {
    "test": [("forward", "arg"), ("reverse", "arg"), ("left", "90"), ("right", "90")],
    "line": [("forward", "arg")],
    "square": [("forward", "arg"), ("left", "90"), ("forward", "arg"), ("left", "90"),
                ("forward", "arg"), ("left", "90"), ("forward", "arg"), ("left", "90")]
}

def forward(distance):
    forward_sm = sub_move()
    forward_sm.primitive.data = "forward"
    forward_sm.distance.data = distance
    forward_sm.angle.data = 0
    pub_sub_move.publish(forward_sm)

def reverse(distance):
    reverse_sm = sub_move()
    reverse_sm.primitive.data = "reverse"
    reverse_sm.distance.data = distance
    reverse_sm.angle.data = 0
    pub_sub_move.publish(reverse_sm)

def left(angle):
    left_sm = sub_move()
    left_sm.primitive.data = "left"
    left_sm.distance.data = 0
    left_sm.angle.data = angle
    pub_sub_move.publish(left_sm)

def right(angle):
    right_sm = sub_move()
    right_sm.primitive.data = "right"
    right_sm.distance.data = 0
    right_sm.angle.data = angle
    pub_sub_move.publish(right_sm)

def send_ack():
    ack = sub_move()
    ack.primitive.data = "ack"
    ack.distance.data = 0
    ack.angle.data = 0
    pub_sub_move.publish(ack)

def next_primitive(data):
    global _continue
    
    print("Siguiente!")
    _continue = True


def decoder(command, argument):
    global _continue, pub_sub_move, start_time, end_time

    start_time = time.time()

    try:
        primitives_list = commands[command]
    except:
        print(f"Command {command} does not exist")
        return

    send_ack()

    for primitive in primitives_list:
        func_name = primitive[0]
        func_arg = int(primitive[1]) if primitive[1] != "arg" else int(argument)
        
        if func_name in globals() and callable(globals()[func_name]):
            func_to_call = globals()[func_name]
            func_to_call(func_arg)
            print("Primitiva enviada")
        else:
            print(f"Function '{func_name}' not found or not callable.")
            return
   
        _continue = False
        while(not _continue):
            pass

    end_time = time.time()
    time_taken = "{:.3f}".format(end_time - start_time)
    rospy.loginfo(f"Finish at: {time_taken}")


if __name__ == "__main__":
    pub_sub_move = rospy.Publisher("sub_move", sub_move, queue_size=10)
    rospy.Subscriber("next_sm", Empty, next_primitive)
    rospy.init_node('locomotion')

    decoder(sys.argv[1], sys.argv[2])


