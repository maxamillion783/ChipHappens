import serial
import serial.tools.list_ports

def open_serial():
    try:
        ports = serial.tools.list_ports.grep('Arduino')
        port = next(ports)
        ser = serial.Serial(port=port, baudrate=9600, timeout=0.1)
        print(f"Serial port {ser.name} opened successfully")
        return ser
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        exit()

if __name__ == '__main__':
    open_serial()
# ###############################################################################