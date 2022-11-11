# import RPi.GPIO as GPIO
from time import time, sleep

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)


TRIGGER4 = 6
ECHO4 = 12

# GPIO.setup(TRIGGER4,GPIO.OUT)
# GPIO.setup(ECHO4,GPIO.IN)

# GPIO.output(TRIGGER4, False)

class Sensor_Four():
    
    def sensor_four():
        
        #SENSOR4
        
        # GPIO.output(TRIGGER4, False)
        print ("Sensor4 Olculuyor...")
        sleep(0.0001)

        # GPIO.output(TRIGGER4, True)
        # sleep(0.00001)
        # GPIO.output(TRIGGER4, False)

        # while GPIO.input(ECHO4)==0:
        #     pulse_start = time()

        # while GPIO.input(ECHO4)==1:
        #     pulse_end = time()

        # pulse_duration = pulse_end - pulse_start
        
        # distance = pulse_duration * 17150
        # distance = round(distance, 2)
        
        # if distance > 2 and distance < 400:
        #     print ("Sensor4 Mesafe:",distance - 0.5,"cm" )
        # else:
        #     print ("Sensor4 Menzil Disi")
        
        sleep(0.005)