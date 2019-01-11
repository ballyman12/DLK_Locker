import pymysql
# Open database connection
db = pymysql.connect("localhost","root","","locker" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql_update = "Update Lockers set DLK_status_Locker = 3"
try:
   # Execute the SQL command
   cursor.execute(sql_update)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
