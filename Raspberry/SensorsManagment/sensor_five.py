# import RPi.GPIO as GPIO
from time import time, sleep

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)


TRIGGER5 = 18
ECHO5 = 4

# GPIO.setup(TRIGGER5,GPIO.OUT)
# GPIO.setup(ECHO5,GPIO.IN)

# GPIO.output(TRIGGER5, False)

class Sensor_Five():
    
    def sensor_five():
        
        #SENSOR5
        
        # GPIO.output(TRIGGER5, False)
        print ("Sensor5 Olculuyor...")
        sleep(0.0001)

        # GPIO.output(TRIGGER5, True)
        # sleep(0.00001)
        # GPIO.output(TRIGGER5, False)

        # while GPIO.input(ECHO5)==0:
        #     pulse_start = time()

        # while GPIO.input(ECHO5)==1:
        #     pulse_end = time()

        # pulse_duration = pulse_end - pulse_start
        
        # distance = pulse_duration * 17150
        # distance = round(distance, 2)
        
        # if distance > 2 and distance < 400:
        #     print ("Sensor5 Mesafe:",distance - 0.5,"cm" )
        # else:
        #     print ("Sensor5 Menzil Disi")
        sleep(0.005)