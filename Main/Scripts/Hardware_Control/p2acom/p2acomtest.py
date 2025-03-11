import serial
import serial.tools.list_ports

if __name__ == '__main__':
    ports = serial.tools.list_ports.grep('Arduino')
    p = next(ports)
    print(p.device)
# ###############################################################################