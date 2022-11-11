#import RPi.GPIO as GPIO
from time import sleep


in1 = 24
in2 = 23
in3 = 27
in4 = 22


# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)

# GPIO.setup(in1, GPIO.OUT)
# GPIO.setup(in2, GPIO.OUT)
# GPIO.setup(in3, GPIO.OUT)
# GPIO.setup(in4, GPIO.OUT)

# GPIO.output(in1, GPIO.LOW)
# GPIO.output(in2, GPIO.LOW)
# GPIO.output(in3, GPIO.LOW)
# GPIO.output(in4, GPIO.LOW)

class Left():
    
    def turn_left_motors():
        print("Turn left")
        # GPIO.output(in1, GPIO.HIGH)
        # GPIO.output(in2, GPIO.LOW)
        # GPIO.output(in3, GPIO.LOW)
        # GPIO.output(in4, GPIO.LOW)
        key = "z"
        return  key