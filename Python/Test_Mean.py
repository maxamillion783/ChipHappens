import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# Function for taking the derivative at each point
# df - dataframe containing the column you want to take the derivative of.
# h - time between data points (SAMPLE_RATE)
# returns an array of the derivatives
# This function only works for data that is formatted correctly
def firstDeriv(df, h):
    n = df.shape[0] # The number of derivatives to take will be the same as the number of rows in the data frame
    deriv = [0]*n # Preallocate the memory for the array

    # One-sided derivatives for beginning and end
    deriv[0] = (-3*df.iloc[0,1]+4*df.iloc[1,1]-df.iloc[2,1])/(2*h)
    deriv[n-1] = (3*df.iloc[n-1,1]-4*df.iloc[n-2,1]+df.iloc[n-3,1])/(2*h)

    # Centered derivative for middle points
    for i, value in enumerate(df["OUT01(mm)"].iloc[1:-1], start=1):
        deriv[i] = (df.iloc[i+1,1]-df.iloc[i-1,1])/(2*h)
        
    return deriv

# TODO: Make this find the relative peaks
def findPeaks(df):
    peaks = []

    for i, value in enumerate(df["Derivatives"].iloc[1:], start=1): # Iterate from the second point to the last point
        if df.iloc[i,1] < 3 and df.iloc[i,1] > 1: # Ignore wildly out of range points
            if value < 0 and df.iloc[i-1, 3] >= 0: # Count peaks where derivative changes from positive to negative
                peaks.append(df.iloc[i,1])

    return peaks

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
file = '../TestData/AP-DATA-004_10-22_trial_1_400mm_1000us_black_solid.csv'
df = pd.read_csv(file, skiprows = 11)

# Display the first few rows of the DataFrame
print(df.head())

# Count peaks
df["Derivatives"] = firstDeriv(df, SAMPLE_RATE) # Add the derivatives to the dataframe
peaks = findPeaks(df) # Create an array of all of the peaks based off of the first derivative
doublePeaks, triplePeaks = meanCounter(peaks, ANGLE)
count = len(peaks) + len(doublePeaks) + 2*len(triplePeaks)

# Output results
print("Total Peaks: " + str(len(peaks)))
print("Double Peaks: " + str(len(doublePeaks)))
print("Triple Peaks: " + str(len(triplePeaks)))
print("Final Count: " + str(count))