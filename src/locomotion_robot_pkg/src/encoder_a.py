#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import UInt64, Bool
import RPi.GPIO as GPIO

# Configura los pines de los encoders
PIN_ENCODER_A1 = 29
PIN_ENCODER_A2 = 31

# Inicializa el contador del encoder
encoder_count = 0
target = 0
counting = False
pub = None

# Variable para almacenar el estado anterior del pin A
last_state_A = None

def callback_encoder_A(channel):
    global encoder_count, last_state_A, counting, pub, target

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

    #print("Enc_A: " + str(encoder_count))

    if encoder_count >= target and counting:
        print("Counted from A!")
        counting = False
        pub.publish(True)

    last_state_A = state_A


def start_counting_cb(data):
    global encoder_count, counting, target
    
    print("Starting counting from A")

    msg = data.data
    encoder_count = 0
    target = int(msg)
    counting = True


if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_ENCODER_A1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PIN_ENCODER_A2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(PIN_ENCODER_A1, GPIO.BOTH, callback=callback_encoder_A)

    rospy.Subscriber('wait_pulses_a', UInt64, start_counting_cb)
    pub = rospy.Publisher("ready_a", Bool, queue_size=10)
    rospy.init_node('encoder_a')
    
    rospy.spin()
