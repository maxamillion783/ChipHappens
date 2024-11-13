import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.signal import find_peaks, butter, filtfilt

# Function which applies a low-pass filter to the data
def lowPass(df, fs):
    cutoff = 75 # cutoff frequency in Hertz
    order = 4  # Filter order
    nyquist = 0.5 * fs  # Nyquist frequency
    normal_cutoff = cutoff / nyquist  # Normalized cutoff frequency

    b, a = butter(order, normal_cutoff, btype='low', analog=False)

    # Apply the filter to the signal using filtfilt (zero-phase filtering)
    filtered_signal = filtfilt(b, a, df["OUT01(mm)"])
    df["Filtered"] = filtered_signal

    # Plot the original and filtered signals
    # plt.figure(figsize=(10, 6))
    # plt.plot(df["Trigger count"], df["OUT01(mm)"], label='Original Signal')
    # plt.plot(df["Trigger count"], df["Filtered"], label='Filtered Signal (Low-Pass)', linewidth=2)
    # plt.xlabel('Time [s]')
    # plt.ylabel('Amplitude')
    # plt.legend()
    # plt.show()

# Find and return peaks and troughs
def findCharacteristics(df):
    peaks = []
    peakIndices, _ = find_peaks(df["Filtered"], distance=25)
    peaks.append(peakIndices)

# Function for counting double and triple peaks based off of the mean
def meanCounter(peaks, theta):
    MIN_THICKNESS = 0.68 # Minimum card thickness based on ISO/IEC 7810 ID-1 standard
    SENSITIVITY = 0.75 # Sensitivity of 0 counts all peaks (at or above mean) as triple peaks, 1 counts only perfectly stacked (thinnest) cards as double peaks

    # Arrays to store all double and triple peaks
    doublePeaks = [] 
    triplePeaks = [] 

    # Calculate tolerances (cutoff values)
    meanHeight = np.mean(peaks)
    doubleCutoff = meanHeight + SENSITIVITY*MIN_THICKNESS*math.cos(math.radians(theta))
    tripleCutoff = meanHeight + 2*SENSITIVITY*MIN_THICKNESS*math.cos(math.radians(theta))

    # Fill in double and triple peak arrays
    for peak in peaks:
        if peak > tripleCutoff:
            triplePeaks.append(peak)
        elif peak > doubleCutoff:
            doublePeaks.append(peak)

    return doublePeaks, triplePeaks

SAMPLE_RATE = 0.001 # Sensor takes data every SAMPLE_RATE seconds
ANGLE = 25 # Angle of the data

# Load the CSV file into a DataFrame
file = '../TestData/AP-DATA-011_11-12_BSC_c=92_d=10_t=1000_v=1000.csv'
df = pd.read_csv(file, skiprows = 11)
df = df[df["OUT01(mm)"] > 0]

# Display the first few rows of the DataFrame
print(df.head())

lowPass(df, 1/SAMPLE_RATE)

# Count peaks
# df["Derivatives"] = firstDeriv(df, SAMPLE_RATE) # Add the derivatives to the dataframe
# peaks = findPeaks(df) # Create an array of all of the peaks based off of the first derivative
# doublePeaks, triplePeaks = meanCounter(peaks, ANGLE)
# count = len(peaks) + len(doublePeaks) + 2*len(triplePeaks)



# Output results
# print(df.head())
print("Total Peaks: " + str(len(peaks)))
# print("Double Peaks: " + str(len(doublePeaks)))
# print("Triple Peaks: " + str(len(triplePeaks)))
# print("Final Count: " + str(count))