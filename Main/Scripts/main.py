#main script to count cards
import sys
import csv
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

# countCards(file)
def countFile(file):
    sensorData, sensorDataQuality = read(file)
    peaks, troughs = findPeaksAndTroughs(sensorData)
    distancesBetweenPeaks, distancesBetweenTroughs = findDistances(peaks, troughs)
    peaksHistogram, troughsHistogram = findHistogram(distancesBetweenPeaks, distancesBetweenTroughs)
    peakCutoffHeight, troughCutoffHeight, expectedPeakAverage, expectedTroughAverage, singlePeakCutoff = findCutoffs(peaks, troughs, peaksHistogram, troughsHistogram, distancesBetweenPeaks, distancesBetweenTroughs, sensorData, sensorDataQuality)
    cardCount = countCards(peaks, troughs, distancesBetweenPeaks, peakCutoffHeight, troughCutoffHeight, expectedPeakAverage, expectedTroughAverage, singlePeakCutoff, sensorData)
    plot = plotData(sensorData, peaks, troughs, troughCutoffHeight, peakCutoffHeight, singlePeakCutoff, peaksHistogram, troughsHistogram)

    return cardCount

count = countFile(file)
input("Press enter to stop script")

# Open the CSV file in append mode
with open("output.csv", "a", newline="") as file:
    writer = csv.writer(file)
    
    # Append the integer as a single value in a new row
    writer.writerow([count])
# NOTE: Hypothesis that counts that are +1 from true are counting holder geometry