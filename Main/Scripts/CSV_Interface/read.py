# read the csv file from the sensor and store it as a data frame
import pandas as pd

file = '../../TestData/AP-DATA-016_11-12_WCC_c=60_d=30_t=1000_v=1000_ma=4_messy.csv'
df = pd.read_csv(file, skiprows = 11)
sensorData = df["OUT01(mm)"]
sensorDataQuality = df.iloc[:,2]