import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.IN)

while True:
    input= GPIO.input(16)

    if(input==1):
        os.system("python3 image_stitch.py -i /home/pi/Desktop/inputimages -o /home/pi/Desktop/outputimages/output")
        time.sleep(5)
    
