import matplotlib.pyplot as plt
import numpy

def processCsv(name):
    fileStr = "../TestData/"+name;
    with open(fileStr, 'r') as f:
        data = [x.strip().split(',') for x in f.readlines()]
    return [x[:2] for x in data[12:]]


if __name__ == "__main__":
    d=processCsv("AP-DATA-006_10-22_trial_3_400mm_1000us_1000Hz_black_solid.csv");
    plt.plot([float(x[1]) for x in d])
    plt.show()