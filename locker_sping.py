import time
import pymysql
import random
import deposit
import mqtt_publish
import paho.mqtt.client as mqtt




global locker_open

def locker_main(RFID_user):

    global check_status
    
    # Open database connection
    db = pymysql.connect("localhost","root","","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor1 = db.cursor()
    cursor2 = db.cursor()
    cursor3 = db.cursor()

    cursor4 = db.cursor()

    cursor5 = db.cursor()

    #RFID_user = (input("ลงชื่อ : ")) ##scan  ควรอยู่ input แรก 

    select_user = "SELECT * FROM access  WHERE DLK_RFID = '%s' and (CURRENT_TIME > DLK_RFID_Start and CURRENT_TIME < DLK_RFID_EXP )  " %(RFID_user)
    cursor.execute(select_user)
    user = cursor.fetchall()
    for row in user :
        Id_User = row[1]
        Start_Date = row[4]
        EXP_Date = row[5]
        



    if(user) :
            # Prepare SQL query to INSERT a record into the database.
            sql_check_blacklist = "SELECT * FROM access where DLK_Id_User = '%d' and DLK_Id_blacklist IS NOT NULL " %(Id_User)



            # Execute the SQL command
            cursor.execute(sql_check_blacklist)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchone()
            # Now print fetched result
            #print (results)
            #print (name[1])
            if(results) :
                print ("ไม่สามารถใช้งานได้ค่ะ กรุณาติดต่อเจ้าหน้าที่")

                
            else :
                
                print ("ยินดีต้อนรับค่ะ")

                sql_check_item = "select * from details where DLK_RFID = '%s' and DLK_Id_Result = 1 " %(RFID_user)
                cursor2.execute(sql_check_item)
                check_item = cursor2.fetchone()

                if(check_item) :
                    print("ตู้ที่ %d" %check_item[3])
                    print("ฝากเพิ่ม / ถอน")

                    # Prepare SQL query to INSERT a record into the database.
                    sql_update = " UPDATE details SET DLK_Date_Curent = CURRENT_TIME() \
                                   WHERE details.DLK_Id_Detail = '%d' AND details.DLK_Id_result = 1 " \
                                   %check_item[0]
                    try:
                       # Execute the SQL command
                       cursor4.execute(sql_update)
                       # Commit your changes in the database
                       db.commit()
                    except:
                       # Rollback in case there is any error
                       db.rollback()

                    locker_open = int(input("เปิดตู้ไหม ? : ")) ## Megnetic door Switch

                    

                    if(locker_open==1) :

                        check_status = 0 #######

                        ## insert log ประตูเปิด

                        # Prepare SQL query to INSERT a record into the database.
                        sql_insert_log = "INSERT INTO log_status_locker(DLK_Id_User , \
                           DLK_RFID, DLK_Number_Locker, DLK_Status_Locker , MQTT_Status) \
                           VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
                           (Id_User,RFID_user,check_item[3], 2 ,0 )
                        try:
                           # Execute the SQL command
                           cursor.execute(sql_insert_log)
                           # Commit your changes in the database
                           db.commit()
                        except:
                           # Rollback in case there is any error
                           db.rollback()

                        ##update locker

                        sql_update_locker = "Update Lockers set DLK_status_Locker = 2 where DLK_Number_Locker = '%d' " %check_item[3] ## เหลือเปลี่ยนสถานะ ล็อคเกอร์
                        try:
                           # Execute the SQL command
                           cursor4.execute(sql_update_locker)
                           # Commit your changes in the database
                           db.commit()
                        except:
                           # Rollback in case there is any error
                           db.rollback()
                    
                        print("ตู้เปิด")
                        print("")
                        i = 1
                        while i<5 :
                            item = int(input("น้ำหนักสัมภาระ :> "))  ## load cell
                            if(item>0) :
                                locker_open = int(input("เปิดตู้ไหม ? : ")) ## Megnetic door Switch
                                print("")
                                if locker_open == 1 :
                                    print("คุณยังไม่ได้ปิดตู้")
                                    print("")
                                    print("กรุณาปิดตู้ด้วยค่ะ")
                                    i=i+1
                                else :
                                    print("ตู้ปิด")
                                    print("คุณได้ฝากสัมภาระเพิ่มเรียบร้อยแล้ว")
                                    # Prepare SQL query to INSERT a record into the database.
                                    sql_update = " UPDATE details SET DLK_Date_Curent = CURRENT_TIME() \
                                                   WHERE details.DLK_Id_Detail = '%d' AND details.DLK_Id_result = 1 " \
                                                   %check_item[0]
                                    try:
                                       # Execute the SQL command
                                       cursor4.execute(sql_update)
                                       # Commit your changes in the database
                                       db.commit()
                                    except:
                                       # Rollback in case there is any error
                                       db.rollback()

                                    ## insert log ประตูปิด

                                    # Prepare SQL query to INSERT a record into the database.
                                    sql_insert_log = "INSERT INTO log_status_locker(DLK_Id_User , \
                                       DLK_RFID, DLK_Number_Locker, DLK_Status_Locker , MQTT_Status) \
                                       VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
                                       (Id_User,RFID_user,check_item[3], 1 ,0 )
                                    try:
                                       # Execute the SQL command
                                       cursor.execute(sql_insert_log)
                                       # Commit your changes in the database
                                       db.commit()
                                    except:
                                       # Rollback in case there is any error
                                       db.rollback()

                                    ##update locker

                                    sql_update_locker = "Update Lockers set DLK_status_Locker = 4 where DLK_Number_Locker = '%d' " %check_item[3] ## เหลือเปลี่ยนสถานะ ล็อคเกอร์
                                    try:
                                       # Execute the SQL command
                                       cursor4.execute(sql_update_locker)
                                       # Commit your changes in the database
                                       db.commit()
                                    except:
                                       # Rollback in case there is any error
                                       db.rollback()

                                   ## insert log ตู้ไม่ว่าง

                                    # Prepare SQL query to INSERT a record into the database.
                                    sql_insert_log = "INSERT INTO log_status_locker(DLK_Id_User , \
                                       DLK_RFID, DLK_Number_Locker, DLK_Status_Locker , MQTT_Status) \
                                       VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
                                       (Id_User,RFID_user,check_item[3], 4 ,0 )
                                    try:
                                       # Execute the SQL command
                                       cursor.execute(sql_insert_log)
                                       # Commit your changes in the database
                                       db.commit()
                                    except:
                                       # Rollback in case there is any error
                                       db.rollback()

                                    print("ขอบคุณที่ใช้บริการค่ะ")
                                    print("")
                                    break
                                    check_status = 1 #######

                            else :
                                print("ถอนสัมภาระ")
                                print("")
                                locker_open = int(input("เปิดตู้ไหม ? : ")) ## Megnetic door Switch
                                print("")
                                if locker_open == 1 :
                                    print("คุณยังไม่ได้ปิดตู้")
                                    print("")
                                    print("กรุณาปิดตู้ด้วยค่ะ")
                                    i=i+1
                                else :
                                    print("คุณได้ถอนฝากสัมภาระเรียบร้อยแล้วคะ")
                                    # Prepare SQL query to INSERT a record into the database.
                                    sql_update = " UPDATE details SET DLK_Date_Curent = CURRENT_TIME() , details.DLK_Id_result = 8  \
                                                   WHERE details.DLK_Id_Detail = '%d'  " \
                                                   %check_item[0]
                                    try:
                                       # Execute the SQL command
                                       cursor4.execute(sql_update)
                                       # Commit your changes in the database
                                       db.commit()
                                    except:
                                       # Rollback in case there is any error
                                       db.rollback()


                                ## insert log ประตูปิด

                                    # Prepare SQL query to INSERT a record into the database.
                                    sql_insert_log = "INSERT INTO log_status_locker(DLK_Id_User , \
                                       DLK_RFID, DLK_Number_Locker, DLK_Status_Locker , MQTT_Status) \
                                       VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
                                       (Id_User,RFID_user,check_item[3], 1 ,0 )
                                    try:
                                       # Execute the SQL command
                                       cursor.execute(sql_insert_log)
                                       # Commit your changes in the database
                                       db.commit()
                                    except:
                                       # Rollback in case there is any error
                                       db.rollback()

                                    ##update locker

                                    sql_update_locker = "Update Lockers set DLK_status_Locker = 3 where DLK_Number_Locker = '%d' " %check_item[3] ## เหลือเปลี่ยนสถานะ ล็อคเกอร์
                                    try:
                                       # Execute the SQL command
                                       cursor4.execute(sql_update_locker)
                                       # Commit your changes in the database
                                       db.commit()
                                    except:
                                       # Rollback in case there is any error
                                       db.rollback()

                                   ## insert log ตู้ว่าง

                                    # Prepare SQL query to INSERT a record into the database.
                                    sql_insert_log = "INSERT INTO log_status_locker(DLK_Id_User , \
                                       DLK_RFID, DLK_Number_Locker, DLK_Status_Locker , MQTT_Status) \
                                       VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
                                       (Id_User,RFID_user,check_item[3], 3 ,0 )
                                    try:
                                       # Execute the SQL command
                                       cursor.execute(sql_insert_log)
                                       # Commit your changes in the database
                                       db.commit()
                                    except:
                                       # Rollback in case there is any error
                                       db.rollback()
                       
                                    print("ขอบคุณที่ใช้บริการค่ะ")
                                    
                                    break

                                    check_status = 1 #######

                        if(i==5 and item>0 ) :
                            print("Report")#
                            print("ไม่ปิดตู้แต่ฝากของอยู่")#
                            # Prepare SQL query to INSERT a record into the database.
                            sql_update = " UPDATE details SET DLK_Date_Curent = CURRENT_TIME() , details.DLK_Id_result = 5  \
                                           WHERE details.DLK_Id_Detail = '%d'  " \
                                           %check_item[0]
                            try:
                               # Execute the SQL command
                               cursor4.execute(sql_update)
                               # Commit your changes in the database
                               db.commit()
                            except:
                               # Rollback in case there is any error
                               db.rollback()
                            print("คุณไม่ได้ปิดตู้ล็อคเกอร์ค่ะ")
                            

                            check_status = 1 #######


                            
                            print("")
                        elif(i==5 and item == 0) :
                            print("Report")#
                            print("ไม่ปิดตู้แต่ถอนของแล้ว")#
                            # Prepare SQL query to INSERT a record into the database.
                            sql_update = " UPDATE details SET DLK_Date_Curent = CURRENT_TIME() , details.DLK_Id_result = 6  \
                                           WHERE details.DLK_Id_Detail = '%d'  " %check_item[0]
                            try:
                               # Execute the SQL command
                               cursor4.execute(sql_update)
                               # Commit your changes in the database
                               db.commit()
                            except:
                               # Rollback in case there is any error
                               db.rollback()
                            print("ขอบคุณที่ใช้บริการค่ะ")
                            print("")

                            check_status = 1 #######
                             

                            
                            
                            
                    else :
                        check_status = 1 #######
                        print("ตู้ปิด")
                        print("ไม่ได้ฝากสัมภาระเพิ่มค่ะ")
                        # Prepare SQL query to INSERT a record into the database.
                        sql_update = " UPDATE details SET DLK_Date_Curent = CURRENT_TIME() \
                                       WHERE details.DLK_Id_Detail = '%d' AND details.DLK_Id_result = 1 " \
                                       %check_item[0]
                        try:
                           # Execute the SQL command
                           cursor4.execute(sql_update)
                           # Commit your changes in the database
                           db.commit()
                        except:
                           # Rollback in case there is any error
                           db.rollback()
                        print("")
                    
                else :
                    print("เริ่มฝาก")

                    deposit.deposit_item(RFID_user,Id_User)
                    


                   

                
    else :
        print("บัตรหมดอายุค่ะ กรุณาติดต่อเจ้าหน้าที่")

        check_status = 1 #######
        



    # disconnect from server
    db.close()
