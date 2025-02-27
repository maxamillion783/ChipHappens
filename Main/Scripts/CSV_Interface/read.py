# read the csv file from the sensor and store it as a data frame
import pandas as pd

"""
@brief Reads sensor data from csv
@param file The relative file path to the csv file
@return sensorData array of sensor readings
@return sensorDataQuality array of sensor data qualities (either ALARM or GO for every data point)
"""
def read(file, returnJourney=False):
    df = pd.read_csv(file) # No longer skipping rows as .csv file format has changed
    sensorData = df.iloc[:,1]
    
    # Iterate over sensorData array to make a sensorDataQuality Array
    sensorDataQuality = ['']*len(sensorData) # Preallocate string array for sensorDataQuality that is the same size as sensorData
    for i, dataPoint in enumerate(sensorData, start=0):
        if dataPoint == -99999: # Note that data is in microns now
            sensorDataQuality[i] = "ALARM"
        else:
            sensorDataQuality[i] = "GO"
    
    if returnJourney:
        sensorData.iloc[::-1].reset_index(drop=True)
        sensorDataQuality.iloc[::-1].reset_index(drop=True)

    return sensorData, sensorDataQuality