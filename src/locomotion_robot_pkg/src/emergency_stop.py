import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)      # Set GPIO mode to BCM
pwm_pin = 22

GPIO.setup(pwm_pin, GPIO.OUT)    # STBY
pwm = GPIO.PWM(pwm_pin, 1) 

# Stop PWM
pwm.stop()

GPIO.cleanup()