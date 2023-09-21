import time
from Physical.physical import *
soil_temperature = [1, 3, 0, 6, 0, 1, 100, 11]
class Temperature:
    def __int__(self):
        print("Run Task do nhiet do")

    def readTemperature(self, ser):
        serial_read_data(ser)
        ser.write(soil_temperature)
        time.sleep(1)
        return serial_read_data(ser)