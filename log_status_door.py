import time
import pymysql
import datetime
import mqtt_publish

def open_door(Id_User,RFID_user,locker) :
    # Open database connection
    db = pymysql.connect("localhost","root","","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()


    # Prepare SQL query to INSERT a record into the database.
    sql_insert_log = "INSERT INTO log_status_locker(DLK_Id_User , \
       DLK_RFID, DLK_Number_Locker, DLK_Status_Locker , MQTT_Status) \
       VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
       (Id_User,RFID_user,locker, 2 ,0 )
    try:
       # Execute the SQL command
       cursor.execute(sql_insert_log)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    last_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    
    mass_open = "log|"+str(Id_User)+"|"+str(RFID_user)+"|"+str(locker)+"|2|"+str(last_time)

    return mass_open 

def close_door(Id_User,RFID_user,locker) :
    # Open database connection
    db = pymysql.connect("localhost","root","","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql_insert_log = "INSERT INTO log_status_locker(DLK_Id_User , \
       DLK_RFID, DLK_Number_Locker, DLK_Status_Locker , MQTT_Status) \
       VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
       (Id_User,RFID_user,locker, 1 ,0 )
    try:
       # Execute the SQL command
       cursor.execute(sql_insert_log)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    last_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    
    mass_close = "log|"+str(Id_User)+"|"+str(RFID_user)+"|"+str(locker)+"|1|"+str(last_time)

    return mass_close

def empty_locker(Id_User,RFID_user,locker):
    # Open database connection
    db = pymysql.connect("localhost","root","","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Prepare SQL query to INSERT a record into the database.
    sql_insert_log = "INSERT INTO log_status_locker(DLK_Id_User , \
       DLK_RFID, DLK_Number_Locker, DLK_Status_Locker , MQTT_Status) \
       VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
       (Id_User,RFID_user,locker, 3 ,0 )
    try:
       # Execute the SQL command
       cursor1.execute(sql_insert_log)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    last_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    
    mass_empty = "log|"+str(Id_User)+"|"+str(RFID_user)+"|"+str(locker)+"|3|"+str(last_time)

    return mass_empty

def busy_locker(Id_User,RFID_user,locker):
    # Open database connection
    db = pymysql.connect("localhost","root","","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Prepare SQL query to INSERT a record into the database.
    sql_insert_log = "INSERT INTO log_status_locker(DLK_Id_User , \
       DLK_RFID, DLK_Number_Locker, DLK_Status_Locker , MQTT_Status) \
       VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
       (Id_User,RFID_user,locker, 4,0 )
    try:
       # Execute the SQL command
       cursor1.execute(sql_insert_log)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    last_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    
    mass_busy = "log|"+str(Id_User)+"|"+str(RFID_user)+"|"+str(locker)+"|4|"+str(last_time)

    return mass_busy

    
    
