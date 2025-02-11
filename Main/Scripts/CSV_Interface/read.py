# read the csv file from the sensor and store it as a data frame
import pandas as pd

"""
@brief Reads sensor data from csv
@param file The relative file path to the csv file
@return sensorData array of sensor readings
@return sensorDataQuality array of sensor data qualities (either ALARM or GO for every data point)
"""
def read(file, returnJourney=False):
    df = pd.read_csv(file, skiprows = 11)
    sensorData = df["OUT01(mm)"]
    sensorDataQuality = df.iloc[:,2]
    
    if returnJourney:
        sensorData.iloc[::-1].reset_index(drop=True)
        sensorDataQuality.iloc[::-1].reset_index(drop=True)

    return sensorData, sensorDataQuality