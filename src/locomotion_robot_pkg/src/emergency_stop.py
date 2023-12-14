import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)  # Set GPIO pin numbering mode to BOARD
STBY_PIN = 22  # Define the pin for STBY on the motor driver

GPIO.setup(STBY_PIN, GPIO.OUT)  # Set STBY pin as an output
stby = GPIO.PWM(STBY_PIN, 1)  # Create PWM object for STBY pin (1Hz)

stby.stop()  # Stop motors by activating standby mode
GPIO.cleanup()  # Clean up GPIO resources