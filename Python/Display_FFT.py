import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import pandas as pd

def processData(fname):
    fileStr = "../TestData/"+fname;
    return pd.read_csv(fileStr, skiprows=11)

if __name__ == "__main__":
    data = processData("AP-DATA-013_11-12_WCC_c=62_d=30_t=1000_v=1000_ma=4.csv")
    
    f = 1000
    n = len(data["OUT01(mm)"][100:])
    fft_values = sp.fft.fft(data["OUT01(mm)"][2000:])
    freq = sp.fft.fftfreq(n, d=(1/f))
    
    #res = np.fft.fft(data[(i-50):])
    #freq = np.fft.fftfreq(len(data[(i-50):]), 0.01)

    plt.plot(freq[:n//2], (np.abs(fft_values[:n//2])/n))
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.show()

    '''
    nfreq = freq[:n//2]
    nfft = np.abs(fft_values[:n//2])/n

    cfreq =0
    c = 0
    for i in range(len(nfreq)):
        if nfft[i] > nfft[i+1]:
            c+=1
        
        if c == 6:
            cfreq = nfreq[i]
            break
    
    print(cfreq)
    '''