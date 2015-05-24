import RPi.GPIO as GPIO
import time


def triggerPin(pin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin,GPIO.OUT)
    #GPIO.cleanup(pin)
    GPIO.output(pin,True)
    "Pin has been triggered"
    time.sleep(2)
    #GPIO.cleanup(pin)
    GPIO.output(pin,False)
    time.sleep(1.5)
