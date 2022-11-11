from msilib.schema import Error

import cv2 as cv
import sys


class Camera:
    
    def camera_control():
        
        try:
            cap = cv.VideoCapture(0)
            
            if not cap.isOpened():
                print("Cannot open camera!")
                sys.exit()
        
            while True:
                #Capture frame by frame
                ret , frame = cap.read()

                #if frame is read correctly -> (ret is true)

                if not ret:
                    print("Cannot receive frame stream. Exiting!")
                    break
                
                #Our operations on the frame come here
                #cvtColor -> change the color of frame
                gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

                #Display the resulting form
                #flip func turn the camera 1-> y-axis , 0-> x-axisq
                cv.imshow("Frame", cv.flip(frame, 1))
                
                #print("camera")
                
                if cv.waitKey(1) == ord("q"):
                    break

        except:
            raise Error
        
        finally:    
            # When everything done, release the capture
            cap.release()
            cv.destroyAllWindows()

cam = Camera.camera_control()
cam