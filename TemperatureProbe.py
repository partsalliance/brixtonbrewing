import os
import glob
import time
import datetime

class TemperatureProbe:
    'Class for each possible temperature probe in this project'

    
    
    def __init__(self):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')


    def read_temp_raw(self):
        base_dir = '/sys/bus/w1/devices/'
        device_folder =glob.glob(base_dir + '28*')[0]
        device_file =device_folder + '/w1_slave'
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
