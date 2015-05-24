import inspect

class HotLiquidTank:
    #HotLiquidTank mode for the mash tun. Heat Water to 5 degrees above Temperature
    #Input of heat element and temp probe, also creation of object with two heat elements
    #need to work out how to check objects are correct
    def __init__(self,tempProbe,heatElementOne):
        self.tempProbe = tempProbe
        self.heatElementOne = heatElementOne

    def heatTo(self,requiredTemperature):
        strikeTemp = requiredTemperature + 5
        self.heatElementOne.TurnElementOn()
        while (self.tempProbe.read_temp()<strikeTemp):
            print "Leave element as strike Temp has not been hit"
        self.heatElementOne.TurnElementOff()
            
        
