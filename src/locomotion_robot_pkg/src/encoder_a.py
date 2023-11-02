#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import UInt64
import RPi.GPIO as GPIO

# Configura los pines de los encoders
PIN_ENCODER_A1 = 29
PIN_ENCODER_A2 = 31

# Inicializa el contador del encoder
encoder_count = 0

# Variable para almacenar el estado anterior del pin A
last_state_A = None

def callback_encoder_A(channel):
    global encoder_count, last_state_A

    # Lee el estado actual del pin A
    state_A = GPIO.input(PIN_ENCODER_A1)

    # Lee el estado actual del pin B
    state_B = GPIO.input(PIN_ENCODER_A2)

    if last_state_A is None:
        last_state_A = state_A
        return

    # Verifica si hubo un cambio en el pin A
    if state_A != last_state_A:
        # Si el pin B está en el mismo estado que el pin A, gira en un sentido
        if state_B == state_A:
            encoder_count += 1
        else:
            encoder_count -= 1

    last_state_A = state_A

def count_a():
    pub = rospy.Publisher('wait_pulses_a', UInt64, queue_size=10)
    rospy.init_node('encoder_a')
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        data = str(encoder_count)
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_ENCODER_A1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PIN_ENCODER_A2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(PIN_ENCODER_A1, GPIO.BOTH, callback=callback_encoder_A)
    try:
        count_a()
    except rospy.ROSInterruptException:
        pass
