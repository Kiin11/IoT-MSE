import time
from Physical.physical import *

class Moisture:
    serial = ""
    def __int__(self,ser):
        print("Moisture")
        self.serial = ser

    def readMoisture(self):
        serial_read_data(self.serial)
        self.serial.write(soil_moisture)
        time.sleep(1)
        print("Moisture",serial_read_data(self.serial))
        return serial_read_data(self.serial)