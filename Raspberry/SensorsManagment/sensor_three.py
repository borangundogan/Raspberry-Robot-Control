# import RPi.GPIO as GPIO
from time import time, sleep

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)


TRIGGER3 = 16
ECHO3 = 13

# GPIO.setup(TRIGGER3,GPIO.OUT)
# GPIO.setup(ECHO3,GPIO.IN)

# GPIO.output(TRIGGER3, False)

class Sensor_Three():
    
    def sensor_three():
            
        #SENSOR3
        
        # GPIO.output(TRIGGER3, False)
        print ("Sensor3 Olculuyor...")
        sleep(0.0001)

        # GPIO.output(TRIGGER3, True)
        # sleep(0.00001)
        # GPIO.output(TRIGGER3, False)

        # while GPIO.input(ECHO3)==0:
        #     pulse_start = time()

        # while GPIO.input(ECHO3)==1:
        #     pulse_end = time()

        # pulse_duration = pulse_end - pulse_start
        
        # distance = pulse_duration * 17150
        # distance = round(distance, 2)
        
        # if distance > 2 and distance < 400:
        #     print ("Sensor3 Mesafe:",distance - 0.5,"cm" )
        # else:
        #     print ("Sensor3 Menzil Disi")

        sleep(0.005)