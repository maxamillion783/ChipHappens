#main script to count cards
import sys
import csv
import serial
script_dir = __file__.rsplit('/', 2)[0]
sys.path.append(script_dir)

from CSV_Interface.read import read
from Data_Processing.Data_Visualization.plotData import plotData
from Data_Processing.findPeaksAndTroughs import findPeaksAndTroughs
from Data_Processing.findDistances import findDistances
from Data_Processing.findHistograms import findHistogram
from Data_Processing.findCutoffs import findCutoffs
from Data_Processing.countCards import countCards
from Data_Processing.Data_Visualization.plotData import plotData
from Sensor_Interface.sensorDataCollection import collectData

#works on these files:
file = '../Test_Data/11-12/AP-DATA-010_11-12_BSC_c=78_d=20_t=1000_v=1000_ma=4.csv'
# file = '../Test_Data/11-12/AP-DATA-016_11-12_WCC_c=60_d=30_t=1000_v=1000_ma=4_messy.csv'
# file = '../Test_Data/11-12/AP-DATA-015_11-12_BSC_c=54_d=30_t=1000_v=1000_ma=4_messy.csv'
# file = '../Test_Data/11-12/AP-DATA-014_11-12_BSC_c=64_d=30_t=1000_v=1000_ma=4.csv'

#does not work:
# file = '../Test_Data/11-12/AP-DATA-009_11-12_WCC_c=75_d=20_t=1000_v=1000_ma=4.csv' # Counted 76
# file = '../Test_Data/11-12/AP-DATA-011_11-12_BSC_c=92_d=10_t=1000_v=1000_ma=4.csv' # Counted 85, 10 degree angle is too low
# file = '../Test_Data/11-12/AP-DATA-012_11-12_WCC_c=89_d=10_t=1000_v=1000_ma=4.csv' # Returns card count of 63, 10 degree angle is too low
# file = '../Test_Data/11-12/AP-DATA-013_11-12_WCC_c=62_d=30_t=1000_v=1000_ma=4.csv' # Counted 63

backFile = file # File generated by the sensor on the return journey

# countCards(file)
def countFile(file, returnJourney=False):
    try:
        ser = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # Replace 'COM3' with your port
        print(f"Serial port {ser.name} opened successfully")
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        exit()
    # Send command to arduino to start running
    ser.write('H'.encode())
    # Call main() in "Sensor Data Collection.py"
    collectionsuccessful = collectData()
    if collectionsuccessful:
        sensorData, sensorDataQuality = read(file, returnJourney)
    else:
        return 0,0,0

    # sensorData, sensorDataQuality = read(file, returnJourney)
    peaks, troughs = findPeaksAndTroughs(sensorData)
    distancesBetweenPeaks, distancesBetweenTroughs = findDistances(peaks, troughs)
    peaksHistogram, troughsHistogram = findHistogram(distancesBetweenPeaks, distancesBetweenTroughs)
    peakCutoffHeight, troughCutoffHeight, expectedPeakAverage, expectedTroughAverage, singlePeakCutoff = findCutoffs(peaks, troughs, peaksHistogram, troughsHistogram, distancesBetweenPeaks, distancesBetweenTroughs, sensorData, sensorDataQuality)
    cardCount = countCards(peaks, troughs, distancesBetweenPeaks, peakCutoffHeight, troughCutoffHeight, expectedPeakAverage, expectedTroughAverage, singlePeakCutoff, sensorData)
    plot = plotData(sensorData, peaks, troughs, troughCutoffHeight, peakCutoffHeight, singlePeakCutoff, peaksHistogram, troughsHistogram)

    return cardCount

def countWithConfidence():
    # Default confidence and error values
    confidence = 100
    errMessage = "Success."

    # Count forward and backward
    print("FORWARD COUNT")
    count, numInvalidPeaks, numDoublePeaks = countFile(file)
    print("\nBACKWARD COUNT")
    backCount, backNumInvalidPeaks, backNumDoublePeaks = countFile(backFile, True) # Count from return journey scan

    # Immediate error if counts don't match
    if count != backCount:
        confidence = 0
        errMessage = "Error. Forward and backward counts do not match. Please try again."
    
    # Compute a confidence based on the number of invalid and double peaks
    # TODO: Consider whether the number of double peaks between counts matches (currently uses an average)
    doubleRate = 5 # Lose 10 confidence points per double peak (20 double peaks results in zero confidence)
    invalidRate = 20 # Lose 20 confidence points per invalid peak (5 invalid peaks results in zero confidence)
    confidence = 100 - doubleRate*(numDoublePeaks + backNumDoublePeaks)/2.0 - invalidRate*(numInvalidPeaks + backNumInvalidPeaks)/2.0
    confidence = max(0, confidence) # Can't have negative percent confidence
    return count, confidence, errMessage

count, confidence, errMessage = countWithConfidence()
# Print out information
print("\nFINAL RESULTS")
print("Count: " + str(count))
print("Confidence: " + str(confidence) + "%")
print("Error Message: " + errMessage)
input("Press enter to stop script")

# Open the CSV file in append mode
with open("output.csv", "a", newline="") as file:
    writer = csv.writer(file)
    
    # Append the integer as a single value in a new row
    writer.writerow([count])
# NOTE: Hypothesis that counts that are +1 from true are counting holder geometry