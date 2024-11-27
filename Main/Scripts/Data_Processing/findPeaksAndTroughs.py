import scipy as sp

"""
@brief finds peaks and troughs in the card data using the scipy.signal.find_peaks function
@param sensorData array containing all of the sensor readings
@return peaks array containing all found peaks
@return troughs array containing all found troughs
"""
def findPeaksAndTroughs(sensorData):
    #find the peaks and troughs of the sensor data using a minimum prominence and distance
    #NOTE: prominence = 0.145 works well for 30 degrees, and 
    peaks, _ = sp.signal.find_peaks(sensorData,prominence=0.125,distance=30)
    troughs, _ = sp.signal.find_peaks(1-sensorData,prominence=0.125,distance=30)

    if troughs[0] < peaks[0]:
        troughs = troughs[1:]

    return peaks, troughs