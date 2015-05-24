from HeatElement import HeatElement
from TemperatureProbe import TemperatureProbe
import time
from decimal import *


h = HeatElement(16,18)
time.sleep(2)
h1 = HeatElement(11,13)
t = TemperatureProbe()
print(t.read_temp() + "hello")
t.activateLogging()

delta = 2.0
striketemp = 82.0

h1.turnElementOn()
time.sleep(1)
h.turnElementOn()
#print (striketemp + " " + delta)

while Decimal(t.read_temp()) < striketemp - delta:
     print t.read_temp() + " inside loop"
     #if (Decimal(t.read_temp()) > striketemp - delta):
       #  h1.turnElementOff()
    
h.turnElementOff()
h1.turnElementOff()
hitStrikeTemp =True
currentTemp = Decimal(t.read_temp())
while currentTemp <= Decimal(t.read_temp()) :
        # "measure over shoot"
        
         currentTemp = Decimal(t.read_temp());
         print "Current temp is: " + t.read_temp()
         
print t.read_temp()
print striketemp
#print (t.read_temp()-striketemp())
print (Decimal(t.read_temp())-Decimal(striketemp))         
time.sleep(1)
#h1.turnElementOff()

t.deactivateLogging()
