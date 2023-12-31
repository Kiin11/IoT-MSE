import time
import serial.tools.list_ports

print("RS485")
print("Sensors and Actuators")

# try:
#     # ls /dev/tty* lenh tim cong com
#     ser = serial.Serial(port="/dev/tty.usbserial-A50285BI", baudrate=9600)
# except:
#     print("Can not open the port")i
relay1_ON = [0, 6, 0, 0, 0, 255, 200, 91]
relay1_OFF = [0, 6, 0, 0, 0, 0, 136, 27]

relay2_ON = [15, 6, 0, 0, 0, 255, 200, 164]
relay2_OFF = [15, 6, 0, 0, 0, 0, 136, 228]

soil_temperature = [1, 3, 0, 6, 0, 1, 100, 11]
soil_moisture = [1, 3, 0, 7, 0, 1, 53, 203]

try:
    # ls /dev/tty* lenh tim cong com
    ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)
except:
    print("Can not open the port")

def setDevice1(ser_arg,state):
    if state:
        ser_arg.write(relay1_ON)
    else:
        ser_arg.write(relay1_OFF)
    time.sleep(1)
    print(serial_read_data(ser_arg))

def setDevice2(ser_arg,state):

    if state:
        ser_arg.write(relay2_ON)
    else:
        ser_arg.write(relay2_OFF)
    time.sleep(1)
    print(serial_read_data(ser_arg))

def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        out = ser.read(bytesToRead)
        data_array = [b for b in out]
        print(data_array)
        if len(data_array) >= 7:
            array_size = len(data_array)
            value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
            return value
        else:
            return -1
    return 0

# while True:
#     setDevice1(True)
#     time.sleep(2)
#     setDevice2(True)
#     time.sleep(2)
#     setDevice1(False)
#     time.sleep(2)
#     setDevice2(False)
#     time.sleep(2)


