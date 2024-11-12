import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import webbrowser

#import numpy as np
#import math

# Load the CSV file into a DataFrame
file = '../TestData/AP-DATA-004_10-22_trial_1_400mm_1000us_black_solid.csv'
df = pd.read_csv(file, skiprows = 11)

# Display the first few rows of the DataFrame
print(df.head())
#print(df['Trigger count'])

# Line plot
fig = px.line(df, x='Trigger count', y='OUT01(mm)', title='Simple Data Visualization')
filename = 'Data Visualization Test.html'
fig.update_layout(
    xaxis_title='Data Number',
    yaxis_title='Distance (mm)'
)
fig.write_html(filename)
webbrowser.open(filename)