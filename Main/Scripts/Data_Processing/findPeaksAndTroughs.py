import scipy as sp
from Data_Processing.truncateBadData import sensorData

#find the peaks and troughs of the sensor data using a minimum prominence and distance
#NOTE: prominence = 0.145 works well for 30 degrees, and 
peaks, _ = sp.signal.find_peaks(sensorData,prominence=0.125,distance=30)
troughs, _ = sp.signal.find_peaks(1-sensorData,prominence=0.125,distance=30)

if troughs[0] < peaks[0]:
    troughs = troughs[1:]

# Check that troughs and peaks arrays line up such that one trough is between each set of peaks (no more, no less)
for i in range(len(peaks) - 1):
    if not (troughs[i] > peaks[i] and troughs[i] < peaks[i+1]):
        print("WARNING: Troughs and peaks do not line up")
        print("Problem peaks: " + str(peaks[i]) + ", " + str(peaks[i+1]))
        print("Problem troughs: " + str(troughs[i]))
        break