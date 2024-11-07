import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Function for creating and displaying the bootstrap distribution of the found peak data
def bootstrapPeaks(file):
    SAMPLE_RATE = 0.001 # Sensor takes data every SAMPLE_RATE seconds

    # Load the CSV file into a DataFrame
    df = pd.read_csv(file, skiprows = 11)

    # Display the first few rows of the DataFrame
    print(df.head())

    # Add the derivatives to the data frame
    df["Derivatives"] = firstDeriv(df, SAMPLE_RATE)

    # Make a histogram of the peaks
    peaks = findPeaks(df)
    numSamples = 3000
    sample = np.random.choice(peaks, size=numSamples, replace=True)
    plt.hist(sample, bins=30, edgecolor='black', color='skyblue')
    plt.show()

bootstrapPeaks('../TestData/AP-DATA-004_10-22_trial_1_400mm_1000us_black_solid.csv')