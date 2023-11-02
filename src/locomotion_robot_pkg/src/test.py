import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)      # Set GPIO mode to BCM


GPIO.cleanup()
GPIO.setup(12, GPIO.OUT)    # PWMA
GPIO.setup(18, GPIO.OUT)    # AIN2
GPIO.setup(16, GPIO.OUT)    # AIN1
GPIO.setup(22, GPIO.OUT)    # STBY

in1 = GPIO.LOW
in2 = GPIO.HIGH
GPIO.output(22, GPIO.HIGH)
GPIO.output(16, in1)
GPIO.output(18, in2)
pwm = GPIO.PWM(12, 1)
pwm.start(100)
pwm.ChangeDutyCycle(100)

while True:
    pass