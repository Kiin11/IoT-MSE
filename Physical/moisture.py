import time
from Physical.physical import *
import view

class Moisture:
    def __int__(self, clientMQTT):
        print("Moisture")
        self.client = clientMQTT

    def readMoisture(self):
        serial_read_data(ser)
        ser.write(soil_moisture)
        time.sleep(1)
        value = serial_read_data(ser)/100
        # view.set_text_value_B(value)
        view.set_text_label_B(value)
        self.client.publish("sensor2",value)
        # return serial_read_data(ser)