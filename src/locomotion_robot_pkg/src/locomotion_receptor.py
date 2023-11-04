#!/usr/bin/env python3
import sys
import rospy
import time
from locomotion_robot_pkg.msg import sub_move

_continue = True
start_time = None
end_time = None
pub_sub_move = None


def next_move_a(data):
    global _continue, start_time, end_time

    end_time = time.time()
    time_taken = "{:.3f}".format(end_time - start_time)
    rospy.loginfo(f"Finish at: {time_taken}")
    
    _continue = False
    #motorStop()

### Main ###
def decoder(command, argument):
    global _continue, pub_sub_move

    print(command)
    print(argument)

    sub_move_1 = sub_move()
    sub_move_1.primitive = str(command)
    sub_move_1.distance = int(argument)
    sub_move_1.angle = 90
    pub_sub_move.publish(sub_move_1)

    rospy.spin()


if __name__ == "__main__":
    pub_sub_move = rospy.Publisher("/mlp/sub_move", sub_move, queue_size=10)
    rospy.init_node('locomotion')

    command = sys.argv[1]
    argument = sys.argv[2]
    #decoder(command, argument)

    sub_move_1 = sub_move()
    sub_move_1.primitive.data = str(command)
    sub_move_1.distance.data = int(argument)
    #sub_move_1.angle.data = 45

    rate = rospy.Rate(1)

    for i in range(20):
        sub_move_1.angle.data = i
        pub_sub_move.publish(sub_move_1)
        rate.sleep()

    rospy.spin()

