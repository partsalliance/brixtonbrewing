
from HeatElement import HeatElement
from TemperatureProbe import TemperatureProbe
import time
from decimal import *

fermHigh = 20.0
fermLow = 18.0
fermLow1 =18.5
h = HeatElement(11,13)
time.sleep(2)
t = TemperatureProbe()
t.activateLogging()
#h.turnElementOn()

while True:
    if(Decimal(t.read_temp()) < fermLow):
        h.turnElementOn()
    elif(Decimal(t.read_temp()) > fermHigh):
        h.turnElementOff()
    print t.read_temp()
    if(fermLow1 <=Decimal(t.read_temp())<= fermHigh):
       if(h.running == True):
           h.turnElementOff()
