import time
from Physical.physical import *
import view
class Temperature:
    def __int__(self):
        print("Run Task do nhiet do")

    def readTemperature(self):
        serial_read_data(ser)
        ser.write(soil_temperature)
        time.sleep(1)
        view.txtA.update(serial_read_data(ser) / 100)
        # return serial_read_data(ser)