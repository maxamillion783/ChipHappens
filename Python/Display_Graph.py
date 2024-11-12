import matplotlib.pyplot as plt
import numpy

def pocessCsv(name):
    with open(name, 'r') as f:
        data = f.readlines()
    print(data)

if __name__ == "__main__":
    pass