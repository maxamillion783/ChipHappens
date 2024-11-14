#Created 11/13/2024 by Cole Barton
#This is the first attempt at counting credit card sleeves

#import necessary libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import webbrowser
import scipy as sp
import numpy as np

# Load the CSV file into a DataFrame
#works on these files:
#file = '../TestData/AP-DATA-016_11-12_WCC_c=60_d=30_t=1000_v=1000_ma=4_messy.csv'
#untested:
file = '../TestData/AP-DATA-015_11-12_BSC_c=54_d=30_t=1000_v=1000_ma=4_messy.csv'
#does not work:
df = pd.read_csv(file, skiprows = 11)

#find the peaks and troughs of the sensor data using a minimum prominence and distance
peaks, _ = sp.signal.find_peaks(df["OUT01(mm)"],prominence=0.145,distance=30)
troughs, _ = sp.signal.find_peaks(1-df["OUT01(mm)"],prominence=0.145)
#print(peaks)

#plot sensor data as a line plot with peaks and troughs
fig = px.line(df, y='OUT01(mm)', title='Data Visualization', markers=True) #sensor data
fig.add_trace(go.Scatter(x=peaks, y=df['OUT01(mm)'][peaks], mode = 'markers', name='Peaks'),) #peaks
fig.add_trace(go.Scatter(x=troughs, y=df['OUT01(mm)'][troughs], mode = 'markers', name='Troughs'),) #troughs
fig_filename = 'Sensor Data with Peaks.html'
fig.update_layout(
    xaxis_title='Data Number',
    yaxis_title='Distance (mm)'
)

#calculate the distance from each peak to its neighbor on the right
distances_between_peaks = np.zeros((len(peaks)-1))
for i in range(0,len(peaks)-1):
    distances_between_peaks[i] = peaks[i+1]-peaks[i]
print(peaks)
print(distances_between_peaks)

#calculate the distance from each trough to its neighbor on the right
distances_between_troughs = np.zeros((len(troughs)-1))
for i in range(0,len(troughs)-1):
    distances_between_troughs[i] = troughs[i+1]-troughs[i]
print(troughs)
print(distances_between_troughs)

#generate peaks and troughs histograms
min_bin = 30
max_bin = 150
size_bin = 2
num_bins = int((max_bin - min_bin) / size_bin)
peaks_histogram = sp.ndimage.histogram(distances_between_peaks,min_bin,max_bin,num_bins)
troughs_histogram = sp.ndimage.histogram(distances_between_troughs,min_bin,max_bin,num_bins)

#plot peaks histogram
fig_peaks_histogram = px.bar(x = range(min_bin,max_bin,size_bin), y=peaks_histogram, title='Peaks Histogram')
fig_peaks_histogram.update_layout(
    xaxis_title='Quantity in Bin',
    yaxis_title='Number of Samples Between Peak and its Right Neighbor'
)
fig_peaks_histogram_filename = 'Peaks Histogram.html'
fig_peaks_histogram.write_html(fig_peaks_histogram_filename)
webbrowser.open(fig_peaks_histogram_filename)
#fig_peaks_histogram.show()

#plot troughs histogram
fig_troughs_histogram = px.bar(x = range(min_bin,max_bin,size_bin), y=troughs_histogram, title='Troughs Histogram')
fig_troughs_histogram.update_layout(
    xaxis_title='Quantity in Bin',
    yaxis_title='Number of Samples Between Trough and its Right Neighbor'
)
fig_troughs_histogram_filename = 'Troughs Histogram.html'
fig_troughs_histogram.write_html(fig_troughs_histogram_filename)
webbrowser.open(fig_troughs_histogram_filename)
#fig_troughs_histogram.show()

#find the most common distance between peaks to figure out how far apart single stacks should be.
#Anything larger than the cutoff will be considered a double peak.
single_peak_distance = np.argmax(peaks_histogram) * size_bin + min_bin
single_peak_cutoff = int(single_peak_distance * 1.5)
single_trough_distance = np.argmax(troughs_histogram) * size_bin + min_bin
single_trough_cutoff = int(single_trough_distance * 1.5)
print(single_peak_cutoff)
print(single_trough_cutoff)

#create an upper bound for peaks to be considered valid, and a lower bound for troughs to be considered valid
num_expected_peaks = 0
expected_peaks_sum = 0
for i in range(0,len(distances_between_peaks)):
    if distances_between_peaks[i] == single_peak_distance:
        num_expected_peaks += 1
        expected_peaks_sum += df['OUT01(mm)'][peaks[i]]
expected_peak_average = expected_peaks_sum/num_expected_peaks

num_expected_troughs = 0
expected_troughs_sum = 0
for i in range(0,len(distances_between_troughs)):
    if distances_between_troughs[i] == single_trough_distance:
        num_expected_troughs += 1
        expected_troughs_sum += df['OUT01(mm)'][troughs[i]]
expected_trough_average = expected_troughs_sum/num_expected_troughs

trough_cutoff = expected_trough_average - (expected_peak_average - expected_trough_average) * 1.0
peak_cutoff = expected_peak_average + (expected_peak_average - expected_trough_average) * 2.5

#add upper and lower bounds to line graph
fig.add_hline(y=expected_peak_average, line_color = 'green')
fig.add_hline(y=expected_trough_average, line_color = 'green')
fig.add_hline(y=peak_cutoff, line_color = 'red')
fig.add_hline(y=trough_cutoff, line_color = 'red')

#Set y-axis range to only observe the valid peaks
fig.update_yaxes(range=[trough_cutoff - 0.5, peak_cutoff + 0.5])

#display line graph
fig.write_html(fig_filename)
webbrowser.open(fig_filename)
#fig.show()

#cound the cards
card_count = 0
num_invalid_peaks = 0
for i in range(0,len(distances_between_peaks)):
    if df['OUT01(mm)'][peaks[i]] < peak_cutoff and df['OUT01(mm)'][peaks[i]] > trough_cutoff:
        if distances_between_peaks[i] < single_peak_cutoff:
            card_count+=1
        else:
            card_count+=2
    else:
        num_invalid_peaks += 1
card_count += 1 #FIXME need a way to tell if the last peak is double or single
print(card_count)
print(num_invalid_peaks)