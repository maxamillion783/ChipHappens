#calculate the distance between peaks and troughs
import scipy as sp
import numpy as np

"""
@brief finds the x distances between peaks and troughs
@param peaks array containing all found peaks
@param troughs array containing all found troughs
@return distancesBetweenPeaks array containing all of the x distances between peaks
@return distancesBetweenTroughs array containing all of the x distances between troughs
"""
def findDistances(peaks, troughs):
    #calculate the distance from each peak to its neighbor on the right
    distancesBetweenPeaks = np.zeros((len(peaks)-1))
    for i in range(0,len(peaks)-1):
        distancesBetweenPeaks[i] = peaks[i+1]-peaks[i]

    #calculate the distance from each trough to its neighbor on the right
    distancesBetweenTroughs = np.zeros((len(troughs)-1))
    for i in range(0,len(troughs)-1):
        distancesBetweenTroughs[i] = troughs[i+1]-troughs[i]
    
    return distancesBetweenPeaks, distancesBetweenTroughs