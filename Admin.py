import time
import pymysql
import random
import locker_sping
import Open_Locker1
import Open_Locker2
import TurnOn_Locker
import mqtt_publish
import paho.mqtt.client as mqtt

def main_using(RFID_user) :

    global check_status

    # Open database connection
    db = pymysql.connect("localhost","root","","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor4 = db.cursor()
    cursor5 = db.cursor()


    #RFID_user = input("ลงชื่อ : ") ##scan  ควรอยู่ input แรก 

    sql_check_admin = "SELECT * FROM access WHERE DLK_RFID = '%s' and DLK_Position_User = 'admin' " %RFID_user
    cursor5.execute(sql_check_admin)
    select_admin = cursor5.fetchall()
    for row in select_admin :
        User = row[1]
        Start_Date = row[4]
        EXP_Date = row[5]
    ##print(User) ส่งค่า

    if(select_admin) :
        select_status = int(input("เลือกสถานะ Admin (0) / User (1) : ")) ##เลือก สถานะก่อนใช้งานสำหรับ Admin
        if(select_status == 0) :
            print("1. ปลดล็อคตู้")
            print("2. ปลดล็อคโดย Admin ผู้เดียว")
            print("3. ระงับการใช้งานของตู้")
            select_menu = int(input("เลือก : "))
            if(select_menu == 1) :
                print("1. ปลดล็อคตู้")
                
                Open_Locker1.open_locker(RFID_user,User)

            elif(select_menu == 2) :
                print("2. ปลดล็อคโดย Admin ผู้เดียว")

                Open_Locker2.open_locker_admin(RFID_user,User)

                
            else :
                print("3. ระงับการใช้งานของตู้")

                TurnOn_Locker.turn_on_locker(RFID_user,User)
                
                
                    
                    

        else :
            locker_sping.locker_main(RFID_user)
    else :
        locker_sping.locker_main(RFID_user)
        
    # disconnect from server
    db.close()
