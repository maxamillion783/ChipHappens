# read the csv file from the sensor and store it as a data frame
import pandas as pd

#works on these files:
#file = '../../TestData/AP-DATA-010_11-12_BSC_c=78_d=20_t=1000_v=1000_ma=4.csv'
file = '../../TestData/AP-DATA-016_11-12_WCC_c=60_d=30_t=1000_v=1000_ma=4_messy.csv'
#untested:

#does not work:
#file = '../../TestData/AP-DATA-015_11-12_BSC_c=54_d=30_t=1000_v=1000_ma=4_messy.csv'
#file = '../../TestData/AP-DATA-009_11-12_WCC_c=75_d=20_t=1000_v=1000_ma=4.csv'
#file = '../../TestData/AP-DATA-011_11-12_BSC_c=92_d=10_t=1000_v=1000_ma=4.csv'

df = pd.read_csv(file, skiprows = 11)
sensorData = df["OUT01(mm)"]
sensorDataQuality = df.iloc[:,2]