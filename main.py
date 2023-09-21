print("Hello AIoT")
import sys
from Adafruit_IO import MQTTClient
from Physical.temperature import *

from scheduler import *

import argparse


AIO_FEED_ID = ["button1", "button2", "sensor1","sensor2","sensor3","equation"]
AIO_USERNAME = "kiin11"
AIO_KEY = ""
global_equation = ""

def main():
    parser = argparse.ArgumentParser(description='Python script with user and password arguments')
    parser.add_argument('-key', required=True, help='Password')
    args = parser.parse_args()

    # Access the arguments
    AIO_KEY = args.key

    print(AIO_KEY)

try:
    # ls /dev/tty* lenh tim cong com
    ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)
except:
    print("Can not open the port")

# camera_detect_model = CameraDetector()

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
    # if feed_id == "button1":
    #     setDevice1(ser,payload == "1")
    # elif feed_id == "button2":
    #     setDevice2(ser,payload == "1")
    if(feed_id == "equation"):
        global_equation = payload
        print(global_equation)

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
scheduler = Scheduler()
scheduler.SCH_Init()

temp = Temperature(ser)
# moisture = readMoisture(ser)


scheduler.SCH_Add_Task(temp,1000,5000)
# scheduler.SCH_Add_Task(moisture,3000,5000)

# main()
while True:
    # Gửi thông số cho các sensor
    # counter = counter - 1
    # if counter <= 0:
    #     counter = 10
    #     #TODO
    #     print("Random data is publish ...")
    #     if sensor_type == 0:
    #         print("Temprerature ...")
    #         temp = random.randint(10,25)
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
    # image_origin, label, _ = camera_detect_model.detect()
    # client.publish("ai", label)

    # client.publish("sensor1", readTemperature(ser)/100)
    # client.publish("sensor2", readMoisture(ser)/100)
    # Lay du lieu

    # equation = init_global_equation()
    #
    # x1 = random.randint(10,30)
    # x2 = random.randint(10,30)
    # x3 = random.randint(10,30)
    #
    # client.publish("sensor4", modify_value(x1,x2,x3, equation))
    #
    # print(x1, x2, x3)
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()

    time.sleep(0.1)

    pass