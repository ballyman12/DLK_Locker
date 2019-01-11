import time
import pymysql

def open_locker(RFID_user,User) :

    global check_status

    # Open database connection
    db = pymysql.connect("localhost","root","","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor4 = db.cursor()
    cursor5 = db.cursor()
    
    i=0
    while i < 3 :

        sql_locker = "SELECT * FROM lockers "
        cursor.execute(sql_locker)
        locker_all = cursor.fetchall()
    
        for row in locker_all :
            locker = row[1]
            # Now print fetched result
            print ("ตู้ที่ = %d" %(locker))

        select_locker = int(input("เลือกตู้ : "))

        select_user = input("ผู้ใช้งานตู้ : ")

        sql_select_detail = "select * from details where DLK_RFID = '%s' and DLK_Number_Locker = '%d' and DLK_Id_Result = 1 " %(select_user , select_locker)
        cursor5.execute(sql_select_detail)
        select_detail = cursor5.fetchone()
        ##print(select_detail[3])

        if(select_detail) :

            check_status = 0  #######

            ## insert log ประตูเปิด

            # Prepare SQL query to INSERT a record into the database.
            sql_insert_log = "INSERT INTO log_status_locker(DLK_Id_User , \
               DLK_RFID, DLK_Number_Locker, DLK_Status_Locker , MQTT_Status) \
               VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
               (User,RFID_user,select_detail[3], 2 ,0 )
            try:
               # Execute the SQL command
               cursor.execute(sql_insert_log)
               # Commit your changes in the database
               db.commit()
            except:
               # Rollback in case there is any error
               db.rollback()

            ##update locker

            sql_update_locker = "Update Lockers set DLK_status_Locker = 2 where DLK_Number_Locker = '%d' " %select_detail[3] ## เหลือเปลี่ยนสถานะ ล็อคเกอร์
            try:
               # Execute the SQL command
               cursor4.execute(sql_update_locker)
               # Commit your changes in the database
               db.commit()
            except:
               # Rollback in case there is any error
               db.rollback()

            
            
            print("ตู้ปลดล็อค")

            locker_open = 1 ## status menetic door

            while locker_open == 1 :
            ## time.sleep(30)

                check_item = int(input("น้ำหนักของ : ")) ##load cell check

            ## ถามว่าปิดตู้ไหม ?

                locker_open = int(input("เปิดตู้ไหม ? : ")) ## Megnetic door Switch

            if(check_item > 0) :

                ## มีของ

                ## insert log ประตูปิด

                # Prepare SQL query to INSERT a record into the database.
                sql_insert_log = "INSERT INTO log_status_locker(DLK_Id_User , \
                   DLK_RFID, DLK_Number_Locker, DLK_Status_Locker , MQTT_Status) \
                   VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
                   (User,RFID_user,select_detail[3], 1 ,0 )
                try:
                   # Execute the SQL command
                   cursor.execute(sql_insert_log)
                   # Commit your changes in the database
                   db.commit()
                except:
                   # Rollback in case there is any error
                   db.rollback()## update detaial user >> detail


                # Prepare SQL query to INSERT a record into the database.
                sql_update = " UPDATE details SET details.DLK_Id_result = 1 \
                               WHERE details.DLK_Id_Detail = '%d' AND details.DLK_RFID = '%s' " \
                               %(select_detail[0] , select_detail[2])
                try:
                   # Execute the SQL command
                   cursor4.execute(sql_update)
                   # Commit your changes in the database
                   db.commit()
                except:
                   # Rollback in case there is any error
                   db.rollback()

                ## insert log ประตูใช้งาน

                # Prepare SQL query to INSERT a record into the database.
                sql_insert_log_2 = "INSERT INTO log_status_locker(DLK_Id_User , \
                   DLK_RFID, DLK_Number_Locker, DLK_Status_Locker , MQTT_Status) \
                   VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
                   (User,RFID_user,select_detail[3], 4 ,0 )
                try:
                   # Execute the SQL command
                   cursor.execute(sql_insert_log_2)
                   # Commit your changes in the database
                   db.commit()
                except:
                   # Rollback in case there is any error
                   db.rollback()## update detaial user >> detail

                ## update status

                sql_update_locker = "Update Lockers set DLK_status_Locker = 4 where DLK_Number_Locker = '%d' " %select_detail[3] ## เหลือเปลี่ยนสถานะ ล็อคเกอร์
                try:
                   # Execute the SQL command
                   cursor4.execute(sql_update_locker)
                   # Commit your changes in the database
                   db.commit()
                except:
                   # Rollback in case there is any error
                   db.rollback()


                

                check_status = 1  #######

                break

            else :

                check_status = 0  #######

                ## ไม่มีของ

                ## insert log ประตูปิด

                

                # Prepare SQL query to INSERT a record into the database.
                sql_insert_log = "INSERT INTO log_status_locker(DLK_Id_User , \
                   DLK_RFID, DLK_Number_Locker, DLK_Status_Locker , MQTT_Status) \
                   VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
                   (User,RFID_user,select_detail[3], 1 ,0 )
                try:
                   # Execute the SQL command
                   cursor.execute(sql_insert_log)
                   # Commit your changes in the database
                   db.commit()
                except:
                   # Rollback in case there is any error
                   db.rollback()
                   
                ##update locker



                ## update status locker >> locker

                sql_update_locker = "Update Lockers set DLK_status_Locker = 3 where DLK_Number_Locker = '%d' " %select_detail[3]
                try:
                   # Execute the SQL command
                   cursor4.execute(sql_update_locker)
                   # Commit your changes in the database
                   db.commit()
                except:
                   # Rollback in case there is any error
                   db.rollback()

                ## insert log ประตูว่างพร้อมใช้งาน

                

                # Prepare SQL query to INSERT a record into the database.
                sql_insert_log_2 = "INSERT INTO log_status_locker(DLK_Id_User , \
                   DLK_RFID, DLK_Number_Locker, DLK_Status_Locker , MQTT_Status) \
                   VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
                   (User,RFID_user,select_detail[3], 3 ,0 )
                try:
                   # Execute the SQL command
                   cursor.execute(sql_insert_log_2)
                   # Commit your changes in the database
                   db.commit()
                except:
                   # Rollback in case there is any error
                   db.rollback()

                ## update detaial user >> detail

                # Prepare SQL query to INSERT a record into the database.
                sql_update = " UPDATE details SET details.DLK_Id_result = 8 \
                               WHERE details.DLK_Id_Detail = '%d' AND details.DLK_RFID = '%s' " \
                               %(select_detail[0] , select_detail[2])
                try:
                   # Execute the SQL command
                   cursor4.execute(sql_update)
                   # Commit your changes in the database
                   db.commit()
                except:
                   # Rollback in case there is any error
                   db.rollback()


                check_status = 1  #######

                break

                    
        else :
            print("เงื่อนไขไม่ตรงกันกรุณาลองอีกครั้ง")
            i=i+1
    # disconnect from server
    db.close()
