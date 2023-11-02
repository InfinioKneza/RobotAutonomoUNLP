#!/usr/bin/env python3
# license removed for brevity

#import sys
#from time import sleep      # Import sleep from time
#import RPi.GPIO as GPIO

# Configura los pines del encoder
#encoder_a1 = 29
#encoder_a2 = 31
#encoder_b1 = 35
#encoder_b2 = 37

# Configura el modo de los pines
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(encoder_a1, GPIO.IN)
#GPIO.setup(encoder_a2, GPIO.IN)
#GPIO.setup(encoder_b1, GPIO.IN)
#GPIO.setup(encoder_b2, GPIO.IN)

#def main():
    #while True:
        #print("-------------------------------------")
        #print("Enconder A1: ", GPIO.input(encoder_a1))
        #print("Enconder A2: ", GPIO.input(encoder_a2))
        #print("Enconder B1: ", GPIO.input(encoder_b1))
        #print("Enconder B2: ", GPIO.input(encoder_b2))


#if __name__ == "__main__":
    #print(sys.argv)
    #main()

import RPi.GPIO as GPIO
import time

# Configura los pines de los encoders
PIN_ENCODER_A = 29
PIN_ENCODER_B = 31

# Inicializa el contador del encoder
encoder_count = 0

# Variable para almacenar el estado anterior del pin A
last_state_A = None

def callback_encoder_A(channel):
    global encoder_count, last_state_A

    # Lee el estado actual del pin A
    state_A = GPIO.input(PIN_ENCODER_A)

    # Lee el estado actual del pin B
    state_B = GPIO.input(PIN_ENCODER_B)

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

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_ENCODER_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PIN_ENCODER_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(PIN_ENCODER_A, GPIO.BOTH, callback=callback_encoder_A)

    try:
        while True:
            print("Encoder Count:", encoder_count)
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
