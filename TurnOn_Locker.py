import time
import pymysql

def turn_on_locker(RFID_user,User) :

    global check_status
    
    # Open database connection
    db = pymysql.connect("localhost","root","","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor4 = db.cursor()
    cursor5 = db.cursor()

    sql_locker = "SELECT * FROM lockers "
    cursor.execute(sql_locker)
    locker_all = cursor.fetchall()
    
    for row in locker_all :
        locker = row[1]
        # Now print fetched result
        print ("ตู้ที่ = %d" %(locker))

    select_locker = int(input("เลือกตู้ : "))

    sql_select_detail = "select * from details where DLK_Number_Locker = '%d' and DLK_Id_Result = 1 " %select_locker
    cursor5.execute(sql_select_detail)
    select_detail = cursor5.fetchone()
    

    if(select_detail):

        

        print("กรุณานำสัมภาระออกจากตู้ฝากของก่อนจากนั้นดำเนินการใหม่อีกครั้งค่ะ มิฉะนั้นจะเกิดความเสียหายต่อทรัพย์สิน")

        

    else :


        update = int(input("เปิดใช้งาน 1 / ระงับใช้งาน 0  :"))

        if(update == 1) :

            check_status = 0  #######
            
            ## insert log ประตูเปิดใช้งาน

            # Prepare SQL query to INSERT a record into the database.
            sql_insert_log = "INSERT INTO log_status_locker(DLK_Id_User , \
               DLK_RFID, DLK_Number_Locker, DLK_Status_Locker , MQTT_Status) \
               VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
               (User,RFID_user,select_locker, 3 ,0 )
            try:
               # Execute the SQL command
               cursor.execute(sql_insert_log)
               # Commit your changes in the database
               db.commit()
            except:
               # Rollback in case there is any error
               db.rollback()
            
            print("เปิด")
            
            # Prepare SQL query to INSERT a record into the database.
            sql_update = " UPDATE lockers SET DLK_Status_Locker = 3 WHERE lockers.DLK_Number_locker = '%d'  " \
                           %select_locker  ## edit
            try:
               # Execute the SQL command
               cursor.execute(sql_update)
               # Commit your changes in the database
               db.commit()
            except:
               # Rollback in case there is any error
               db.rollback()

            check_status = 1  #######

            
        else :

            check_status = 0  #######

            ## insert log ประตูระงับใช้งาน
            
            print("ระงับ")
            # Prepare SQL query to INSERT a record into the database.
            sql_update = " UPDATE lockers SET DLK_Status_Locker = 5 \
                           WHERE lockers.DLK_Number_locker = '%d'  " \
                           %select_locker
            try:
               # Execute the SQL command
               cursor.execute(sql_update)
               # Commit your changes in the database
               db.commit()
            except:
               # Rollback in case there is any error
               db.rollback()

               
            # Prepare SQL query to INSERT a record into the database.
            sql_insert_log = "INSERT INTO log_status_locker(DLK_Id_User , \
               DLK_RFID, DLK_Number_Locker, DLK_Status_Locker , MQTT_Status) \
               VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
               (User,RFID_user,select_locker, 5 ,0 )
            try:
               # Execute the SQL command
               cursor.execute(sql_insert_log)
               # Commit your changes in the database
               db.commit()
            except:
               # Rollback in case there is any error
               db.rollback()

            check_status = 1  #######

    # disconnect from server
    db.close()
