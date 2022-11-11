
import sys


sys.path.append(r"C:\Users\red_h\OneDrive\Masaüstü\Raspberry\Raspberry\MoveManagement")
sys.path.append(r"C:\Users\red_h\OneDrive\Masaüstü\Raspberry\Raspberry\SensorsManagment")
sys.path.append(r"C:\Users\red_h\OneDrive\Masaüstü\Raspberry\Raspberry\CameraManagment")

import MoveManagement.move as m
import threading
import multiprocessing

import SensorsManagment.sensor_one as s1
import SensorsManagment.sensor_two as s2
import SensorsManagment.sensor_three as s3
import SensorsManagment.sensor_four as s4
import SensorsManagment.sensor_five as s5

import CameraManagment.camera as cam

from time import sleep
#import RPi.GPIO as GPIO

class Main():

    def camera():
        cam.Camera.camera_control() 
        
    def main():
        #GPIO.setwarnings(False)

        print("r-run s-stop w-forward x-backward d-right a-left l-low m-medium h-high e-exit")
        print("\n")
        
        try:
            while True:

                decision_controller = input("Choose your decision: ")

                if (decision_controller == "r" or decision_controller == "s" or decision_controller == "w" or decision_controller == "x" or
                    decision_controller == "d" or decision_controller == "a" or decision_controller == "l" or decision_controller == "m" or decision_controller == "h"):
                    m.Move.move(decision_controller)
                    s1.Sensor_One.sensor_one()
                    s2.Sensor_Two.sensor_two()
                    s3.Sensor_Three.sensor_three()
                    s4.Sensor_Four.sensor_four()
                    s5.Sensor_Five.sensor_five()
    
                elif (decision_controller != "e"):
                    print("Undefined command. Please try again!")
                    continue

                else:
                    print("break the code")
                    break
                
        except BaseException:
            raise BaseException

        finally:
            #GPIO.cleanup()
            sleep(0.05)
            print("----Finished----")

if __name__ == "__main__":
    # __camera = Main.camera()
    # __main = Main.main()
    
    __main = multiprocessing.Process(target=Main.main(), args=(10,0))
    __camera = multiprocessing.Process(target=Main.camera(), args=(10, 0))
    #__ = threading.Thread(target=((Main.main(), Main.camera())),  args=(10,0))
    
    __main.start()
    __camera.start()
    
    __main.join()
    __camera.join()
    
    # __.start()
    # __.join()