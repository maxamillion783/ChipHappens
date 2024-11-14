import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import webbrowser
import scipy as sp
import numpy as np
#import math

# Load the CSV file into a DataFrame
#file = '../TestData/AP-DATA-001_trial_1_400mm_1000us_flat.csv'
#file = '../TestData/AP-DATA-002_trial_2_400mm_1000us_stuck.csv'
#file = '../TestData/AP-DATA-003_trial_3_400mm_1000us_less_stuck.csv'
file = '../TestData/AP-DATA-004_10-22_trial_1_400mm_1000us_black_solid.csv'
#file = '../TestData/AP-DATA-005_10-22_trial_2_400mm_1000us_black_solid.csv'
#file = '../TestData/AP-DATA-006_10-22_trial_3_400mm_1000us_1000Hz_black_solid.csv'
#file = '../TestData/AP-DATA-007_10-22_trial_4_400mm_1000us_1000Hz_white_clear.csv'
#file = '../TestData/AP-DATA-008_10-22_trial_5_400mm_1000us_1000Hz_ambient-filter_white-clear.csv'
df = pd.read_csv(file, skiprows = 11)

# Display the first few rows of the DataFrame
#print(df.head())
#print(df['Trigger count'])
#print(df['Trigger count'])

from scipy.signal import find_peaks
peaks, _ = find_peaks(df["OUT01(mm)"],prominence=0.15)
#print(peaks)

# Line plot
fig = px.line(df, y='OUT01(mm)', title='Simple Data Visualization', markers=True)
#fig.add_trace(px.scatter(peaks, x=df['OUT01(mm)'][peaks], y=peaks))
fig.add_trace(go.Scatter(x=peaks, y=df['OUT01(mm)'][peaks], mode = 'markers', name='Peaks'),)
filename = 'Data Visualization Test.html'
fig.update_layout(
    xaxis_title='Data Number',
    yaxis_title='Distance (mm)'
)
fig.write_html(filename, full_html = True)

sampling_rate = 1000 #Hz
fft_values = sp.fft.fft(df['OUT01(mm)'])
#print(fft_values)

# Step 2: Get the frequency bins
n = len(df['OUT01(mm)'])  # Number of samples
frequencies = sp.fft.fftfreq(n, d=1/sampling_rate)

# Step 3: Compute the amplitude spectrum (magnitude of FFT values)
amplitudes = np.abs(fft_values) / n  # Normalize amplitude

# Step 4: Plot the positive frequencies (since FFT is symmetric around 0)
fig_fft = go.Figure()

fig_fft.add_trace(go.Scatter(
    x=frequencies[:n//2],        # Plot only the positive half of frequencies
    y=amplitudes[:n//2],         # Corresponding amplitudes
    mode='lines',
    name='Frequency vs Amplitude'
))

# Update layout for better readability
fig_fft.update_layout(
    title="Frequency vs Amplitude",
    xaxis_title="Frequency (Hz)",
    yaxis_title="Amplitude",
    xaxis=dict(tickformat=".1f"),
    yaxis=dict(tickformat=".2f"),
    template="plotly_white"
)

fig_fft.write_html(filename, full_html = False)
webbrowser.open(filename)

#perform FFT to find the period
#create a moving average over the last 5 periods (to account for deflection)
#subtract the moving average from the data frame to normalize the height
#detect a large jump in height
#detect peaks with a minimum distance of 0.7 periods between them
#if the distance between a peak's 2 neighbors is close to 2 periods, add 1 to the count.
#if the distance between a peak's 2 neighbors is close to 3 periods, add 2 to the count. etc.
