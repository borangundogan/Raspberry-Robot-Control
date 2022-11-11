# import RPi.GPIO as GPIO
from time import time, sleep

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)


TRIGGER2 = 26
ECHO2 = 19

# GPIO.setup(TRIGGER2,GPIO.OUT)
# GPIO.setup(ECHO2,GPIO.IN)

# GPIO.output(TRIGGER2, False)

class Sensor_Two():
    
    def sensor_two():
        
        #SENSOR2
        
        # GPIO.output(TRIGGER2, False)
        print ("Sensor2 Olculuyor...")
        sleep(0.0001)

        # GPIO.output(TRIGGER2, True)
        # sleep(0.00001)
        # GPIO.output(TRIGGER2, False)

        # while GPIO.input(ECHO2)==0:
        #     pulse_start = time()

        # while GPIO.input(ECHO2)==1:
        #     pulse_end = time()

        # pulse_duration = pulse_end - pulse_start
        
        # distance = pulse_duration * 17150
        # distance = round(distance, 2)
        
        # if distance > 2 and distance < 400:
        #     print ("Sensor2 Mesafe:",distance - 0.5,"cm" )
        # else:
        #     print ("Sensor2 Menzil Disi")
        
        sleep(0.005)