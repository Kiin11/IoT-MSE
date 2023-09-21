import time
from Physical.physical import *
import view

class Moisture:
    def __int__(self):
        print("Moisture")

    def readMoisture(self):
        serial_read_data(ser)
        ser.write(soil_moisture)
        time.sleep(1)
        view.txtB.update(serial_read_data(ser) / 100)
        # return serial_read_data(ser)