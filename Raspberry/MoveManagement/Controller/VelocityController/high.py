#High velocity

#import RPi.GPIO as GPIO
from time import sleep

en = 25
enl = 17

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)

#   p = GPIO.PWM(en , 1000)
#   p1 = GPIO.PWM(enl , 1000)

class High():
    
    def high_velocity():
        print("High mode")
        # p.ChangeDutyCycle(75)
        # p1.ChangeDutyCycle(75)
        key = "z"
        return key