import Sensor_Interface.CL3wrap as CL3wrap
import ctypes
import sys
import time
import numpy as np
import os

# Define output path for saving measurement data
output_path = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "output_files"

def collectData(ser):
    deviceId = 0  # Set to "0" if using only one controller
    ethernetConfig = CL3wrap.CL3IF_ETHERNET_SETTING()
    # IP address for Colton's computer now. Will change to LattePanda later
    ethernetConfig.abyIpAddress[0] = 169  
    ethernetConfig.abyIpAddress[1] = 254  
    ethernetConfig.abyIpAddress[2] = 63   
    ethernetConfig.abyIpAddress[3] = 100  
    ethernetConfig.wPortNo = 24685        
    timeout = 10000 
    samples = []  # Array for storeing measurement values
    measurementDataAll = []  # Array for saving data to .csv
    
    # Establish Ethernet communication with the device
    res = CL3wrap.CL3IF_OpenEthernetCommunication(deviceId, ethernetConfig, timeout)
    print("CL3wrap.CL3IF_OpenEthernetCommunication:", CL3wrap.CL3IF_hex(res))
    if res != 0:
        print("Failed to connect to controller.")
        sys.exit()  # Exit if connection fails
    print("----")
###############################################################################
    while (~(ser.in_waiting > 0)):
        measurementData = CL3wrap.CL3IF_MEASUREMENT_DATA()
        res = CL3wrap.CL3IF_GetMeasurementData(deviceId, measurementData)
        print("CL3wrap.CL3IF_GetMeasurementData:",
                CL3wrap.CL3IF_hex(res), "\n",
                "triggerCount:", measurementData.addInfo.triggerCount, "\n",
                "pulseCount:", measurementData.addInfo.pulseCount, "\n")
        
        for j in range(1):  
            print("OUT", j+1, "\n",
                    "measurementValue:", measurementData.outMeasurementData[j].measurementValue, "\n")
            samples.append(measurementData.outMeasurementData[j].measurementValue)
        
        measurementDataAll.append(measurementData)  
        print("----")

    # Convert collected data into a NumPy array for easier manipulation
    n_measurementData = np.zeros((len(measurementDataAll), CL3wrap.NUMBER_OF_OUT_TO_BE_STORED))

    for i in range(len(measurementDataAll)):
        for j in range(CL3wrap.NUMBER_OF_OUT_TO_BE_STORED):
            n_measurementData[i, j] = measurementDataAll[i].outMeasurementData[j].measurementValue

    # Save measurement data to a CSV file for future analysis
    np.savetxt(output_path + "/trendData_measurementData.csv", n_measurementData, fmt='%d', delimiter=",")       
    print("----")

    # Close communication with the device
    res = CL3wrap.CL3IF_CloseCommunication(deviceId)
    print("CL3wrap.CL3IF_CloseCommunication:", CL3wrap.CL3IF_hex(res))

    if (ser.readline().decode().strip() == '1'):
        return 1
    else:
        return 0

# Run the script when executed
if __name__ == '__main__':
    collectData()
