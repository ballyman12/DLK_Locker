import paho.mqtt.client as mqtt
import time
host = "broker.mqttdashboard.com"
port = 8000

location = 1
site = 1
locker_main = 1

topic = "DLK/"+str(location)+"/"+str(site)+"/"+str(locker_main)


def mqtt_publish(mass):
    count = 0
    while True :
        count =count+1
        print('%s , %s ' %(topic,mass))
        client = mqtt.Client()
        client.connect(host)
        client.publish(topic,count)

        time.sleep(1)

