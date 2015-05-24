import RPi.GPIO as GPIO
import time
import unittest

#simply turns the second socket on and off
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(11,False)
time.sleep(5)
GPIO.output(11,True)
time.sleep(5)
GPIO.output(11,False)
time.sleep(5)
print("done")


GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(13,False)
time.sleep(5)
GPIO.output(13,True)
time.sleep(5)
GPIO.output(13,False)
time.sleep(5)
print("done")


#simply turns the second socket on and off
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(16,False)
time.sleep(5)
GPIO.output(16,True)
time.sleep(5)
GPIO.output(16,False)
time.sleep(5)
print("done")


GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(18,False)
time.sleep(5)
GPIO.output(18,True)
time.sleep(5)
GPIO.output(18,False)
time.sleep(5)
print("done")


