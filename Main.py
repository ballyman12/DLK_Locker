
from threading import Thread
import time
import Admin
import deposit
import mqtt_publish
import paho.mqtt.client as mqtt



def input_user() :

    
    

    while True :
            
            RFID_user = (input("ลงชื่อ : ")) ##scan  ควรอยู่ input แรก
            Admin.main_using(RFID_user)
            time.sleep(5)


def check_locker() :
    
    global check_status  ## 1 = ไม่มีคนใช้งาน
    global locker_open

    if(check_status == 1):
        print("เช็คตู้ 1-9")  ## Menetic Sensor
    else :
        print("Waiting Process")

thread1 = Thread(target=input_user)
thread1.start()
