import time
from Physical.physical import *

class Moisture:
    def __int__(self):
        print("Moisture")

    def readMoisture(self):
        serial_read_data(serial)
        serial.write(soil_moisture)
        time.sleep(1)
        print("Moisture",serial_read_data(serial))
        return serial_read_data(serial)