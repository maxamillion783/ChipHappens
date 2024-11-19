import matplotlib.pyplot as plt
import numpy

def processCsv(name):
    fileStr = "../TestData/"+name;
    with open(fileStr, 'r') as f:
        data = [x.strip().split(',') for x in f.readlines()]
    return [x[:2] for x in data[12:]]


if __name__ == "__main__":
    d=processCsv("AP-DATA-014_11-12_BSC_c=64_d=30_t=1000_v=1000_ma=4.csv");
    plt.plot([float(x[1]) for x in d])
    plt.show()