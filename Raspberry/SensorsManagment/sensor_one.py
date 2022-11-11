# import RPi.GPIO as GPIO
import time

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)


TRIGGER1 = 20
ECHO1 = 21

#  GPIO.setup(TRIGGER1,GPIO.OUT)
#  GPIO.setup(ECHO1,GPIO.IN)

# GPIO.output(TRIGGER1, False)

class Sensor_One():
    
    def sensor_one():
        
        #SENSOR1
        
        # GPIO.output(TRIGGER1, False)
        print ("Sensor1 Olculuyor...")
        time.sleep(0.0001)

        # GPIO.output(TRIGGER1, True)
        # time.sleep(0.00001)
        # GPIO.output(TRIGGER1, False)

        # while GPIO.input(ECHO1)==0:
        #     pulse_start = time.time()

        # while GPIO.input(ECHO1)==1:
        #     pulse_end = time.time()

        # pulse_duration = pulse_end - pulse_start
        
        # distance = pulse_duration * 17150
        # distance = round(distance, 2)
        
        # if distance > 2 and distance < 400:
        #     print ("Sensor1 Mesafe:",distance - 0.5,"cm" )
        # else:
        #     print ("Sensor1 Menzil Disi")
        
        time.sleep(0.005)
        