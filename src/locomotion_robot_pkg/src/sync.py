#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64
from simple_pid import PID
from locomotion_robot_pkg.msg import sync_type, motor_speeds
from constants import SYNC_TIME

# Inicialización de los PID
pid_motor = PID(Kp=1, Ki=0, Kd=1, setpoint=0)

# Initialize encoder counters
encoder_a_count = 0
encoder_b_count = 0
current_sync_mode = 0  # Type of the currect syncronization (0 -> regular) (1 -> weighted)
motor_a_speed = 50  # Saves the initial motor A speed
motor_b_speed = 50  # Saves the initial motor B speed

# Initialize flags
count_a_received = False
count_b_received = False

def sync_motors():
    """""Sync motors."""""
    global encoder_a_count, encoder_b_count, count_a_received, count_b_received
    global current_sync_mode, motor_a_speed, motor_b_speed, pub_speed

    # If regular syncronization
    if current_sync_mode == 0:
        # Calculate difference between encoder counts
        difference = abs(encoder_a_count) - abs(encoder_b_count)

        correction = pid_motor(difference, SYNC_TIME)

        # No make any correction if difference is too small
        if abs(difference) < 100:
            return
        
        if correction == 0:
            return
        
        print(f'Encoder difference: {difference} !!!!!')
        print(f'Correction: {correction}')

        last_a_speed = motor_a_speed

        speed_change = float(correction/7500)

        # Speed adjustment
        motor_a_speed = min(100, max(0, motor_a_speed + speed_change))  # Limit within 0 and 100
        motor_b_speed = min(100, max(0, motor_b_speed - speed_change))  # Limit within 0 and 100

        if (last_a_speed != motor_a_speed):
            motor_speeds_msg = motor_speeds()
            motor_speeds_msg.vel_a.data = motor_a_speed
            motor_speeds_msg.vel_b.data = motor_b_speed
            pub_speed.publish(motor_speeds_msg)
    elif current_sync_mode == 1:
        pass  # TODO

    count_a_received = False
    count_b_received = False


def get_encoder_count_a(data):
    """""Get encoder count from A."""""
    global encoder_a_count, count_a_received

    encoder_a_count = int(data.data)
    count_a_received = True

    if count_b_received:
        sync_motors()

    return encoder_a_count

def get_encoder_count_b(data):
    """""Get encoder count from B."""""
    global encoder_b_count, count_b_received

    encoder_b_count = int(data.data)
    count_b_received = True

    if count_a_received:
        sync_motors()

    return encoder_b_count

def sync_update_cb(sync_msg):
    global current_sync_mode

    _sync_type = int(sync_msg.sync_type.data)  # Get sync type
    current_sync_mode = _sync_type  # Set sync type for current movement
    
    if _sync_type == 0:
        pass
    elif _sync_type == 1:
        # For weighted syncronization, use in curve movements
        factor = float(sync_msg.factor.data)
        dominant_motor = int(sync_msg.dominant_motor.data)


if __name__ == '__main__':
    # Create subscribers
    rospy.Subscriber('encoder_count_a', Int64, get_encoder_count_a)
    rospy.Subscriber('encoder_count_b', Int64, get_encoder_count_b)
    rospy.Subscriber("sync_update", sync_type, sync_update_cb)

    # Create publishers
    pub_speed = rospy.Publisher("speed_update", motor_speeds, queue_size=10)

    # Initialize node
    rospy.init_node('sync')

    rospy.spin()
