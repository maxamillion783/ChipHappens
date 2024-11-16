import scipy as sp
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from CSV_Interface.read import sensorData

#find the peaks and troughs of the sensor data using a minimum prominence and distance
#NOTE: prominence = 0.145 works well for 30 degrees, and 
peaks, _ = sp.signal.find_peaks(sensorData,prominence=0.125,distance=30)
troughs, _ = sp.signal.find_peaks(1-sensorData,prominence=0.125,distance=30)