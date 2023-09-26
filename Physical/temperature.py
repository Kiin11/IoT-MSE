import time
from Physical.physical import *
import view

from Adafruit_IO import MQTTClient

class Temperature:
    def __int__(self, clientMQTT = None):
        print("Run Task do nhiet do")
        self.clientMQTT = clientMQTT

    def readTemperature(self):
        serial_read_data(ser)
        ser.write(soil_temperature)
        time.sleep(1)
        value = serial_read_data(ser)/100
        view.set_text_value_A(value)
        self.clientMQTT.publish("sensor1",value)
        # return serial_read_data(ser)