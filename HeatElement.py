class HeatElement:
    'Class for heat Element that will be linked to two GPIO pins'

    def __init__(self,gpioOn,gpioOff):
        self.gpioOn = gpioOn
        self.gpioOff = gpioOff
        self.running = False;
        'check both gpio pins are off'

    def turnElementOn(self):
        'check gpio and running'
        
        if(self.running):
            #print "element already on"
            return "element already on"
        else:
            ' run gpio to turn it on'
            'call element to be on with pin from creation'
            self.running = True
            print "Heat Element has been turned on"

    def turnElementOff(self):
          if(self.running==False):
              return "element already off"
          else:
              self.running = False
              print "Heat Element has been turned off"
    
