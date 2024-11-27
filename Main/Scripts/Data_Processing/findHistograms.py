from Settings_Interface.readSettings import histogramSettings
import scipy as sp

"""
@brief creates a histogram of the distances between peaks and between troughs
@param distancesBetweenPeaks array containing all of the x distances between peaks
@param distancesBetweenTroughs array containing all of the x distances between troughs
@return peaksHistogram histogram of all peak widths
@return troughsHistogram histogram of all trough widths 
"""
def findHistogram(distancesBetweenPeaks, distancesBetweenTroughs):
    #generate peaks and troughs histograms
    numBins = int((histogramSettings["maxBin"] - histogramSettings["minBin"]) / histogramSettings["binSize"])
    peaksHistogram = sp.ndimage.histogram(distancesBetweenPeaks,histogramSettings["minBin"],histogramSettings["maxBin"],numBins)
    troughsHistogram = sp.ndimage.histogram(distancesBetweenTroughs,histogramSettings["minBin"],histogramSettings["maxBin"],numBins)

    return peaksHistogram, troughsHistogram