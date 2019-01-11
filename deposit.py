import time
import pymysql
import datetime
import random
import paho.mqtt.client as mqtt
import log_status_door
import mqtt_publish

host = "broker.mqttdashboard.com"
port = 8000


location = 1
site = 1
locker_main = 1

mqtt_u = "intninlab_pub"
mqtt_p = "intninlab_pub.."


topic = "DLK/"+str(location)+"/"+str(site)+"/"+str(locker_main)




def deposit_item(RFID_user,Id_User) :

    global check_status

    # Open database connection
    db = pymysql.connect("localhost","root","","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    sql_select_locker = "select DLK_Number_Locker from lockers where DLK_status_Locker = 3 "
    cursor.execute(sql_select_locker)
    select_locker = cursor.fetchall()
    #print(select_locker)
    loc_ker = []
    for row in select_locker:
      locker = row[0]
      # Now print fetched result
      #print ("locker = %d" %(locker))
      loc_ker.append(row[0])
    #print(loc_ker)
    locker = random.choice(loc_ker)
    print("ตู้ที่ : %d" %locker)

    ##check_cancel = int(input("ยกเลิกไหม ? (1) หรือ ไม่ยกเลิก (0) >>> : "))

    ##if(check_cancel == 0) :
    
    locker_open = int(input("เปิดตู้ไหม ? : ")) ## Megnetic door Switch

    if(locker_open==1) :

        check_status = 0  #######

        ## insert log ประตูเปิด

        log_status_door.open_door(Id_User,RFID_user,locker)

        mass_open = log_status_door.open_door(Id_User,RFID_user,locker)

        mqtt_publish.mqtt_publish(mass_open)
        
        #print('%s , %s ' %(topic,mass_open))
        #client = mqtt.Client()
        #client.connect(host)
        #client.publish(topic,mass_open)
        

        

        ##update locker

        sql_update_locker = "Update Lockers set DLK_status_Locker = 2 where DLK_Number_Locker = '%d' " %locker ## เหลือเปลี่ยนสถานะ ล็อคเกอร์
        try:
           # Execute the SQL command
           cursor.execute(sql_update_locker)
           # Commit your changes in the database
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()
    
        print("ตู้เปิด")
        print("")
        print("กรุณาฝากสัมภาระ")
        i = 1
        while i<3 :
            item = int(input("น้ำหนักสัมภาระ :> "))  ## load cell
            if(item>0) :
                locker_open = int(input("เปิดตู้ไหม ? : ")) ## Megnetic door Switch
                print("")
                if locker_open == 1 :
                    print("คุณยังไม่ได้ปิดตู้")
                    print("")
                    print("กรุณาปิดตู้ค่ะ")
                    i=i+1
                else :
                    print("ตู้ปิด")

                    ## insert log ประตูปิด

                    log_status_door.close_door(Id_User,RFID_user,locker)

                    mass = log_status_door.close_door(Id_User,RFID_user,locker)

                    #mqtt_publish.mqtt_publish(mass)

                   
                     # Prepare SQL query to INSERT a record into the database.
                    sql_insert = "INSERT INTO Details(DLK_Id_User , \
                       DLK_RFID , DLK_Number_Locker, DLK_id_Result) \
                       VALUES ('%d', '%s', '%d', '%d' )" % \
                       (Id_User,RFID_user,locker, 1)
                    try:
                       # Execute the SQL command
                       cursor.execute(sql_insert)
                       # Commit your changes in the database
                       db.commit()
                    except:
                       # Rollback in case there is any error
                       db.rollback()

                     # Prepare SQL query to INSERT a record into the database.
                    sql_update = "Update Lockers set DLK_status_Locker = 4 where DLK_Number_Locker = ('%d') " %locker
                    try:
                       # Execute the SQL command
                       cursor.execute(sql_update)
                       # Commit your changes in the database
                       db.commit()
                    except:
                       # Rollback in case there is any error
                       db.rollback()


                   ## insert log ตู้ไม่ว่าง

                    log_status_door.busy_locker(Id_User,RFID_user,locker)

                    mass = log_status_door.busy_locker(Id_User,RFID_user,locker)

                    #mqtt_publish.mqtt_publish(mass)

                    


                    
                   
                       
                    print("คุณได้ฝากสัมภาระเรียบร้อยแล้ว")
                    print("ขอบคุณที่ใช้บริการค่ะ")
                    print("")
                    break

                    check_status = 1 #######

            else :
                print("ไม่ได้ฝากของ")
                print("")
                locker_open = int(input("เปิดตู้ไหม ? : ")) ## Megnetic door Switch
                print("")
                if locker_open == 1 :
                    print("คุณยังไม่ได้ปิดตู้")
                    print("")
                    print("กรุณาปิดตู้ค่ะ")
                    i=i+1
                else :

                    print("ตู้ปิด")

                    ## insert log ประตูปิด

                    log_status_door.close_door(Id_User,RFID_user,locker)
                    
                    mass = log_status_door.close_door(Id_User,RFID_user,locker)

                    #mqtt_publish.mqtt_publish(mass)
                    

                   # Prepare SQL query to INSERT a record into the database.
                    sql_update = "Update Lockers set DLK_status_Locker = 3 where DLK_Number_Locker = ('%d') " %locker
                    try:
                       # Execute the SQL command
                       cursor.execute(sql_update)
                       # Commit your changes in the database
                       db.commit()
                    except:
                       # Rollback in case there is any error
                       db.rollback()


                   ## insert log ตู้ว่าง

                    log_status_door.empty_locker(Id_User,RFID_user,locker)
                    
                    mass = log_status_door.close_door(Id_User,RFID_user,locker)

                    #mqtt_publish.mqtt_publish(mass)

                    check_cancel = int(input("ยกเลิกเพราะ ? (1) หรือ ไม่ฝากแล้ว (0) >>> : "))
                    if(check_cancel == 0) :
                         # Prepare SQL query to INSERT a record into the database.
                        sql_insert = "INSERT INTO Details(DLK_Id_User , \
                           DLK_RFID,DLK_Number_Locker, DLK_id_Result) \
                           VALUES ('%d', '%s', '%d', '%d' )" % \
                           (Id_User,RFID_user, locker, 8 )
                        try:
                           # Execute the SQL command
                           cursor.execute(sql_insert)
                           # Commit your changes in the database
                           db.commit()
                        except:
                           # Rollback in case there is any error
                           db.rollback()
                        print("คุณไม่ได้ฝากสัมภาระ")
                        print("ขอบคุณที่ใช้บริการค่ะ")
                        print("")
                        break

                        check_status = 1 #######
                    else :
                        sql_select_condi = "select * from conditions "
                        cursor.execute(sql_select_condi)
                        select_condi = cursor.fetchall()
                        #print(select_locker)
                        
                        for row in select_condi:
                          num_con = row[0]  
                          condi = row[1]                             
                          # Now print fetched result
                          print ("%d = %s" %(num_con , condi))
                          
                          
                        cancel = int(input("ยกเลิกเพราะ ?  >>> : "))
                        # Prepare SQL query to INSERT a record into the database.
                        sql_insert = "INSERT INTO Details(DLK_Id_User , \
                           DLK_RFI,DLK_Number_Locker, DLK_id_Result, DLK_Id_condi) \
                           VALUES ('%d', '%s', '%d','%d' , '%d' )" % \
                           (Id_User , RFID_user , locker, 7 ,cancel )
                        try:
                           # Execute the SQL command
                           cursor.execute(sql_insert)
                           # Commit your changes in the database
                           db.commit()
                        except:
                           # Rollback in case there is any error
                           db.rollback()
                        print("ขอบคุณที่ใช้บริการค่ะ")
                        print("")
                        
                        break

                        check_status = 1 #######
                    
        if i==3 and item > 0 :
            
            check_status = 1 #######
            
            print("Report")#
            print("Report")#
            print("ไม่ปิดตู้แต่ฝากของอยู่")#
            # Prepare SQL query to INSERT a record into the database.
            sql_insert = "INSERT INTO Details(DLK_Id_User , \
               DLK_RFID , DLK_Number_Locker, DLK_id_Result) \
               VALUES ('%d', '%s', '%d', '%d' )" % \
               (Id_User, RFID_user , locker, 5 )
            try:
               # Execute the SQL command
               cursor.execute(sql_insert)
               # Commit your changes in the database
               db.commit()
            except:
               # Rollback in case there is any error
               db.rollback()
            

            #report ผ่านทางโทรศัพท์มือถือ,ไลน์, email
       
        elif i==5 and item == 0 :

            check_status = 1 #######
            
            print("ไม่ปิดตู้ไม่ฝากของ")#
            print("")
            # Prepare SQL query to INSERT a record into the database.
            sql_insert = "INSERT INTO Details(DLK_Id_User , \
               DLK_RFID , DLK_Number_Locker, DLK_id_Result) \
               VALUES ('%d', '%s', '%d', '%d' )" % \
               (Id_User, RFID_user , locker, 6 )
            try:
               # Execute the SQL command
               cursor.execute(sql_insert)
               # Commit your changes in the database
               db.commit()
            except:
               # Rollback in case there is any error
               db.rollback()

        
            
                #report ผ่านทางโทรศัพท์มือถือ,ไลน์, email
        

            
            
    else :
        print("ตู้ปิด")
        print("คุณไม่ได้ทำการเปิดตู้")
        # Prepare SQL query to INSERT a record into the database.
        sql_insert = "INSERT INTO Details(DLK_Id_User , \
           DLK_RFID, DLK_Number_Locker, DLK_id_Result) \
           VALUES ('%d', '%s', '%d', '%d' )" % \
           (Id_User , RFID_user, locker, 8)
        try:
           # Execute the SQL command
           cursor.execute(sql_insert)
           # Commit your changes in the database
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()
        print("ไม่ได้ฝากสัมภาระ")
        print("ขอบคุณที่ใช้บริการค่ะ")

        check_status = 1 #######

#def mqtt_publish(mass):

    
    #print(mass)
    #print(topic)
    #client = mqtt.Client()
    #client.connect(host)
    
    #client.publish(topic,mass)
    #client.publish("DLK/1/1/1","Hello")



