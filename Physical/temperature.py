import time
from Physical.physical import *
class Temperature:
    ser = ""
    def __int__(self, ser):
        print("Run Task do nhiet do")
        self.ser = ser

    def readTemperature(self):
        serial_read_data(self.ser)
        self.ser.write(soil_temperature)
        time.sleep(1)
        print("Temperature",serial_read_data(self.ser))
        return serial_read_data(self.ser)