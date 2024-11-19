import json

with open('../Settings/dataVisualizationSettings.json') as f:
    dataVisulaizationSettings = json.load(f)
with open('../Settings/histogramSettings.json') as f:
    histogramSettings = json.load(f)