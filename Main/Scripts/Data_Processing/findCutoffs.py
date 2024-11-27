import numpy as np
from Settings_Interface.readSettings import histogramSettings

"""
@brief findCutoffs uses the histograms to determine the cutoff values for the card counter
@param peaks array containing all found peaks
@param troughs array containing all found troughs
@param peaksHistogram histogram of all peak widths
@param troughsHistogram histogram of all trough widths 
@param distancesBetweenPeaks array containing all of the x distances between peaks
@param distancesBetweenTroughs array containing all of the x distances between troughs
@param sensorData array containing all of the sensor readings
@param sensorDataQuality array of sensor data qualities (either ALARM or GO for every data point)
@return peakCutoffHeight height above which peaks are considered invalid
@return troughCutoffHeight height below which troughs are considered invalid
@return expectedPeakAverage expected distance between peaks for one card
@return expectedTroughAverage expected distance between troughs for one card
@return singlePeakCutoff distance betweeen peaks at which peaks begin to be double counted
"""
def findCutoffs(peaks, troughs, peaksHistogram, troughsHistogram, distancesBetweenPeaks, distancesBetweenTroughs, sensorData, sensorDataQuality):
    #find the most common distance between peaks to figure out how far apart single stacks should be.
    #Anything larger than the cutoff will be considered a double peak.
    singlePeakDistance = np.argmax(peaksHistogram) * histogramSettings["binSize"] + histogramSettings["minBin"]
    singlePeakCutoff = int(singlePeakDistance * 1.5)
    singleTroughDistance = np.argmax(troughsHistogram) * histogramSettings["binSize"] + histogramSettings["minBin"]
    singleTroughCutoff = int(singleTroughDistance * 1.5)
    print("Average distance between peaks: ", singlePeakDistance)


    #create an upper bound for peaks to be considered valid, and a lower bound for troughs to be considered valid
    numExpectedPeaks = 0
    expectedPeaksSum = 0
    for i in range(0,len(distancesBetweenPeaks)):
        if distancesBetweenPeaks[i] == singlePeakDistance:
            numExpectedPeaks += 1
            expectedPeaksSum += sensorData[peaks[i]]
    expectedPeakAverage = expectedPeaksSum/numExpectedPeaks

    numExpectedTroughs = 0
    expectedTroughsSum = 0
    for i in range(0,len(distancesBetweenTroughs)):
        if distancesBetweenTroughs[i] == singleTroughDistance and sensorDataQuality[troughs[i]] == 'GO':
            numExpectedTroughs += 1
            expectedTroughsSum += sensorData[troughs[i]]
    expectedTroughAverage = expectedTroughsSum/numExpectedTroughs

    troughCutoffHeight = expectedTroughAverage - (expectedPeakAverage - expectedTroughAverage) * 1.0
    peakCutoffHeight = expectedPeakAverage + (expectedPeakAverage - expectedTroughAverage) * 2.5

    return peakCutoffHeight, troughCutoffHeight, expectedPeakAverage, expectedTroughAverage, singlePeakCutoff