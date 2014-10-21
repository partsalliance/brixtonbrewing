import os
import glob
import time
import datetime
import threading
import csv
class TemperatureProbe:
    'Class for each possible temperature probe in this project'

    
    
    def __init__(self):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        self.activeLogging = False

    def read_temp_raw(self):
        base_dir = '/sys/bus/w1/devices/'
        device_folder =glob.glob(base_dir + '28*')[0]
        device_file =device_folder + '/w1_slave'
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
    'return c trimmed to 3 digits'		
    def read_temp(self):
        lines = self.read_temp_raw()

        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp = str(round(temp_c,1))
            #temp = temp_c[0:3]
            #temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp
    'start a new method to start logging the temperature to a csv file'
    def writeToCSV(self):
        with open('test.csv','wb') as fp:
            while (self.activeLogging==True):
                
                a = csv.writer(fp)
                data = [time.strftime("%d/%m/%Y"),time.strftime("%H:%M:%S"),self.read_temp()]
                print (time.strftime("%d/%m/%Y")+ time.strftime("%H:%M:%S") + self.read_temp())
                a.writerows(data)
            a.close()
            print("Thread is dead")

    def activateLogging(self):
        if(self.activeLogging==False):
            'new thread'
            self.activeLogging = True
           # thread.start_new_thread(self.writeToCSV(),())
            t1 = threading.Thread(target=self.writeToCSV)
            t1.start()

    def deactivateLogging(self):
        if(self.activeLogging):
            self.activeLogging = False
            print "Logging has been deactivated on the temperature probe"
        else:
            print "No action taken as the probe was not logging"


   
