import random
import time

print("Hello AIoT")
import sys
from Adafruit_IO import MQTTClient
import cv2  # Install opencv-python
from simpleAI import *
from physical import *

# try:
#     # ls /dev/tty* lenh tim cong com
#     ser = serial.Serial(port="/dev/tty.usbserial-A50285BI", baudrate=9600)
# except:
#     print("Can not open the port")

camera_detect_model = CameraDetector()

AIO_FEED_ID = ["button1", "button2"]
AIO_USERNAME = "kiin11"
AIO_KEY = "aio_ThpH34nUZUqpwpS4VMaBnrYKXQUW"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " , feed id :" + feed_id)
    if feed_id == "button1":
        setDevice1(ser,payload == "1")
    elif feed_id == "button2":
        setDevice2(ser,payload == "1")

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
counter_ai = 5
sensor_type = 0
ai_result = ""
previous_result = ""

while True:
    # Gửi thông số cho các sensor
    # counter = counter - 1
    # if counter <= 0:
    #     counter = 10
    #     #TODO
    #     print("Random data is publish ...")
    #     if sensor_type == 0:
    #         print("Temprerature ...")
    #         temp = random.randint(10,20)
    #         client.publish("sensor1", temp)
    #     if sensor_type == 1:
    #         print("Humi ...")
    #         humi = random.randint(50,70)
    #         client.publish("sensor2", humi)
    #     if sensor_type == 2:
    #         print("Light ...")
    #         light = random.randint(100,500)
    #         client.publish("sensor3", light)
    #
    #     sensor_type = sensor_type+1

    #Gửi thông số cho AI thông qua webcam
    image_origin, label, _ = camera_detect_model.detect()
    client.publish("ai", label)

    # client.publish("sensor1", readTemperature(ser)/100)
    # client.publish("sensor2", readMoisture(ser)/100)
    # Lay du lieu
    time.sleep(5)

    pass