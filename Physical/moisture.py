import time
from Physical.physical import *

class Moisture:
    def __int__(self):
        print("Moisture")

    def readMoisture(self, ser):
        serial_read_data(ser)
        ser.write(soil_moisture)
        time.sleep(1)
        return serial_read_data(ser)