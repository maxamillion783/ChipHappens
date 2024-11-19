import numpy as np
from Settings_Interface.readSettings import histogramSettings
from Data_Processing.findPeaksAndTroughs import peaks,troughs
from Data_Processing.findHistograms import peaksHistogram, troughsHistogram
from Data_Processing.findDistances import distancesBetweenPeaks, distancesBetweenTroughs
from CSV_Interface.read import sensorData, sensorDataQuality

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