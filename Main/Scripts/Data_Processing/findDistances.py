#calculate the distance between peaks and troughs
import scipy as sp
import numpy as np
from Data_Processing.findPeaksAndTroughs import peaks,troughs

#calculate the distance from each peak to its neighbor on the right
distancesBetweenPeaks = np.zeros((len(peaks)-1))
for i in range(0,len(peaks)-1):
    distancesBetweenPeaks[i] = peaks[i+1]-peaks[i]

#calculate the distance from each trough to its neighbor on the right
distancesBetweenTroughs = np.zeros((len(troughs)-1))
for i in range(0,len(troughs)-1):
    distancesBetweenTroughs[i] = troughs[i+1]-troughs[i]