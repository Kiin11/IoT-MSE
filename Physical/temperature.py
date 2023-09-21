import time
from Physical.physical import *
class Temperature:
    def __int__(self):
        print("Run Task do nhiet do")

    def readTemperature(self):
        serial_read_data(ser)
        ser.write(soil_temperature)
        time.sleep(1)
        print("Temperature",serial_read_data(ser))
        return serial_read_data(ser)