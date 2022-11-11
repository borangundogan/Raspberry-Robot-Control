#Move Codes

#import RPi.GPIO as GPIO

import sys

sys.path.append(r"C:\Users\red_h\OneDrive\Masaüstü\Raspberry\Raspberry\MoveManagement\Controller\MoveController")
sys.path.append(r"C:\Users\red_h\OneDrive\Masaüstü\Raspberry\Raspberry\MoveManagement\Controller\VelocityController")

from time import sleep

import Controller.MoveController.backward as backward
import Controller.MoveController.forward as forward
import Controller.MoveController.left as left
import Controller.MoveController.right as right
import Controller.MoveController.stop as stop

import Controller.VelocityController.high as high
import Controller.VelocityController.medium as medium
import Controller.VelocityController.low as low

class Move():

    def move(key):
        
        default_situation = 1
        if key == "r":
            
            print("run")
            
            if default_situation == 1:
                forward.Forward.forward_motors()
            else:
                backward.Backward.backward_motors()

        elif key == "s":
            stop.Stop.stop_motors()

        elif key == "w":
            forward.Forward.forward_motors()

        elif key == "x":
            backward.Backward.backward_motors()

        elif key == "d":
            right.Right.turn_right_motors()

        elif key == "a":
            left.Left.turn_left_motors()

        elif key == "l":
            low.Low.low_velocity()

        elif key == "m":
            medium.Medium.medium_velocity()

        elif key == "h":
            high.High.high_velocity()

# m = Move.move("s")
# m