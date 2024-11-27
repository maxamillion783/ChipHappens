#create a plot showing the sensor data, peaks, etc.
import matplotlib.pyplot as plt
from Settings_Interface.readSettings import dataVisulaizationSettings, histogramSettings

"""
@brief Plots data based on which plots are turned on in the data visualization settings
@param sensorData array containing all of the sensor readings
@param peaks array containing all found peaks
@param troughs array containing all found troughs
@param troughCutoffHeight height below which troughs are considered invalid
@param peakCutoffHeight height above which peaks are considered invalid
@param singlePeakCutoff distance betweeen peaks at which peaks begin to be double counted
@param peaksHistogram histogram of all peak widths
@param troughsHistogram histogram of all trough widths 
"""
def plotData(sensorData, peaks, troughs, troughCutoffHeight, peakCutoffHeight, singlePeakCutoff, peaksHistogram, troughsHistogram):
    #create raw data plot with peaks, troughs, cutoffs, etc.
    plt.figure("Raw Data")
    if dataVisulaizationSettings["showPlots"]["sensorData"]:
        plt.plot(sensorData, label="Sensor Data", color=dataVisulaizationSettings["colors"]["sensorData"])
    if dataVisulaizationSettings["showPlots"]["peaks"]:
        plt.scatter(x=peaks, y=sensorData[peaks], label="Peaks", color=dataVisulaizationSettings["colors"]["peaks"])
    if dataVisulaizationSettings["showPlots"]["troughs"]:
        plt.scatter(x=troughs, y=sensorData[troughs], label="Troughs", color=dataVisulaizationSettings["colors"]["troughs"])
    if dataVisulaizationSettings["showPlots"]["peakCutoffHeight"]:
        plt.axhline(y=peakCutoffHeight, color=dataVisulaizationSettings["colors"]["peakCutoffHeight"], linestyle=dataVisulaizationSettings["lineStyles"]["peakCutoffHeight"], label='Peak Cutoff Height')
    if dataVisulaizationSettings["showPlots"]["troughCutoffHeight"]:
        plt.axhline(y=troughCutoffHeight, color=dataVisulaizationSettings["colors"]["troughCutoffHeight"], linestyle=dataVisulaizationSettings["lineStyles"]["troughCutoffHeight"], label='Trough Cutoff Height')
    if dataVisulaizationSettings["resizePlots"]["zoomIn"]:
        plt.ylim(troughCutoffHeight-0.1,peakCutoffHeight+0.1)
    plt.title("Raw Data")
    plt.xlabel("Index")
    plt.ylabel("Distance")
    plt.legend()

    #create peak histogram plot
    if dataVisulaizationSettings["showPlots"]["peakHistogram"]:
        plt.figure("Peaks Histogram")
        plt.bar(range(histogramSettings["minBin"],histogramSettings["maxBin"],histogramSettings["binSize"]), peaksHistogram, label='Peaks Histogram')
        plt.title("Peaks Histogram")
        plt.xlabel("Distance Between Peak and its Right Neighbor")
        plt.ylabel("Number of Points in Bin")
        plt.axvline(x=singlePeakCutoff, color='red', linestyle='--', label='Single Peak Cutoff')
        plt.legend()

    #create trough histogram plot
    if dataVisulaizationSettings["showPlots"]["troughHistogram"]:
        plt.figure("Troughs Histogram")
        plt.bar(range(histogramSettings["minBin"],histogramSettings["maxBin"],histogramSettings["binSize"]), troughsHistogram, label='Troughs Histogram')
        plt.title("Troughs Histogram")
        plt.xlabel("Distance Between Trough and its Right Neighbor")
        plt.ylabel("Number of Points in Bin")
        plt.legend()

    #make it so the code still runs while the plot is open
    plt.show(block=False)