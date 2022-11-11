#Low velocity 

#import RPi.GPIO as GPIO
from time import sleep

en = 25
enl = 17

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)

# p = GPIO.PWM(en , 1000)
# p1 = GPIO.PWM(enl , 1000)

class Low():

    def low_velocity():
        print("low mode")
        # p.ChangeDutyCycle(25)
        # p1.ChangeDutyCycle(25)
        x = "z"