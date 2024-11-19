import numpy as np
from Data_Processing.findPeaksAndTroughs import peaks,troughs
from Data_Processing.findDistances import distancesBetweenPeaks
from Data_Processing.findCutoffs import peakCutoffHeight, troughCutoffHeight,expectedPeakAverage,expectedTroughAverage,singlePeakCutoff,singleTroughCutoff
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from CSV_Interface.read import sensorData
from enum import Enum

class peakType(Enum):
    INVALID = 0
    SINGLE = 1
    DOUBLE = 2

#count the cards
cardCount = 0
numInvalidPeaks = 0
numDoublePeaks = 0
peakTypes = np.zeros(len(peaks),dtype=int)
for i in range(0,len(distancesBetweenPeaks)):
    if sensorData[peaks[i]] < peakCutoffHeight and sensorData[peaks[i]] > troughCutoffHeight:
        if sensorData[peaks[i]] - sensorData[troughs[i]] > 1.3 * (expectedPeakAverage - expectedTroughAverage) and distancesBetweenPeaks[i] > singlePeakCutoff:
            cardCount+=2
            numDoublePeaks += 1
            peakTypes[i] = peakType.DOUBLE.value
        else:
            cardCount += 1
            peakTypes[i] = peakType.SINGLE.value
    else:
        peakTypes[i] = peakType.INVALID.value
        numInvalidPeaks += 1
peakTypes[len(peaks)-1] = peakType.SINGLE.value #FIXME need a way to tell if the last peak is double or single
cardCount += 1 #FIXME need a way to tell if the last peak is double or single
print("Card Count: ", cardCount)
print("Invalid Peaks: ", numInvalidPeaks)
print("Double Peaks: ", numDoublePeaks)