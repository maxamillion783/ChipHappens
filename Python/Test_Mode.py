import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, butter, filtfilt
from scipy import stats

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

def modeCounter(peaks):
    count = len(peaks) - 1

    # Count the distances between peaks
    distance = [0]*(len(peaks)-1)

    for i in range(len(peaks)-1):
        distance[i] = peaks[i+1]-peaks[i]

    # plt.hist(distance, bins=30, edgecolor='black', color='skyblue')
    # plt.show()

    mode_value = stats.mode(distance, keepdims=True)[0][0]
    print(mode_value)

    doubleCuttoff = mode_value*1.5
    tripleCuttoff = mode_value*2.5

    for i in range(len(distance)):
        if distance[i] >= tripleCuttoff: 
            count = count + 2
        elif distance[i] >= doubleCuttoff:
            count = count + 1 
    print("Count:" + str(count))


SAMPLE_RATE = 0.001 # Sensor takes data every SAMPLE_RATE seconds
ANGLE = 25 # Angle of the data

# Load the CSV file into a DataFrame
file = '../TestData/AP-DATA-015_11-12_BSC_c=54_d=30_t=1000_v=1000_ma=4_messy.csv'
df = pd.read_csv(file, skiprows = 11)
df = df[df["OUT01(mm)"] > -3] # TODO: Switch this to filtering out ALARM rows
lowPass(df, 1/SAMPLE_RATE)

peaks, peakProperties = find_peaks(df["OUT01(mm)"], distance=25, prominence=0.125)
modeCounter(peaks)