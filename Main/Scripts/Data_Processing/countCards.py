import numpy as np

# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from enum import Enum

class peakType(Enum):
    INVALID = 0
    SINGLE = 1
    DOUBLE = 2
"""
@brief Counts the number of cards in a data set
@param peaks array containing all found peaks
@param troughs array containing all found troughs
@param distancesBetweenPeaks array containing all of the x distances between peaks
@param peakCutoffHeight height above which peaks are considered invalid
@param troughCutoffHeight height below which troughs are considered invalid
@param expectedPeakAverage expected distance between peaks for one card
@param expectedTroughAverage expected distance between troughs for one card
@param singlePeakCutoff distance betweeen peaks at which peaks begin to be double counted
@param sensorData array containing all of the sensor readings
@return cardCount a total card count
"""
def countCards(peaks, troughs, distancesBetweenPeaks, peakCutoffHeight, troughCutoffHeight, expectedPeakAverage, expectedTroughAverage, singlePeakCutoff, sensorData):
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

    return cardCount