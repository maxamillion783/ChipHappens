from Settings_Interface.readSettings import histogramSettings
import scipy as sp

def findHistogram(distancesBetweenPeaks, distancesBetweenTroughs):
    #generate peaks and troughs histograms
    numBins = int((histogramSettings["maxBin"] - histogramSettings["minBin"]) / histogramSettings["binSize"])
    peaksHistogram = sp.ndimage.histogram(distancesBetweenPeaks,histogramSettings["minBin"],histogramSettings["maxBin"],numBins)
    troughsHistogram = sp.ndimage.histogram(distancesBetweenTroughs,histogramSettings["minBin"],histogramSettings["maxBin"],numBins)

    return peaksHistogram, troughsHistogram