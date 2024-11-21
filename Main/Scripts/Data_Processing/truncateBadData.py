import pandas as pd
from CSV_Interface.read import df

# Function that linearly interpolates between two points
# x1 - x component of first point
# y1 - y component of first point
# x2 - x component of second point
# y2 - y component of second point
# Returns interpolatedX - an array of points between x1 and x2
# Returns interpolatedY - an array of points between y1 and y2
def linearlyInterpolate(x1, y1, x2, y2):
    n = x2 - x1
    interpolatedX = [0]*(n-1)
    interpolatedY = [0]*(n-1)

    ySpacing = (y2-y1)/(x2-x1)

    for i in range(n-1):
        xn = x1 + i + 1
        yn = y1 + ySpacing*(xn-x1)

        interpolatedX[i] = xn
        interpolatedY[i] = yn

    return interpolatedX, interpolatedY

# Remove all ALARMS at the beginning of our data
# Initialize an index counter
start_index = 0

# Loop through the rows to find the first non-"ALARM" entry
for i in range(len(df)):
    if df.iloc[i, 2] == 'ALARM':
        start_index = i + 1  # Update to next row
    else:  # Break as soon as we encounter a non-"ALARM"
        break

# Drop rows from the start to `start_index` (excluding the break point)
df = df.iloc[start_index:].reset_index(drop=True)

# Iterate over sensor data to find ALARMS between sensor data
x1 = 0
x2 = 0
y1 = 0
y2 = 0
for i in range(len(df)-1):
    # Switching from GO to ALARM indicates a start point for interpolator
    if df.iloc[i+1,2] == 'ALARM' and df.iloc[i,2] == 'GO':
        x1 = i
        y1 = df.iloc[i, 1]
    # Switching from ALARM to GO indicates an end point for interpolator
    elif df.iloc[i+1,2] == 'GO' and df.iloc[i, 2] == 'ALARM':
        x2 = i
        y2 = df.iloc[i, 1]

        interpolatedX, interpolatedY = linearlyInterpolate(x1, y1, x2, y2)
        df.iloc[interpolatedX, df.columns.get_loc('OUT01(mm)')] = interpolatedY

sensorData = df["OUT01(mm)"]
sensorDataQuality = df.iloc[:,2]