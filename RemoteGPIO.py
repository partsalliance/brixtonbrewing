import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


GPIO.setup(16,GPIO.OUT)
GPIO.output(16,1)
#state  = GPIO.input(16)
#print state

t = GPIO.output(16,GPIO.input(16))
print t

GPIO.cleanup(16)

