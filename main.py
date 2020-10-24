import sqlite3
import datetime
import calendar
from sqlite3 import Error

############################################################
#               CHEAT SHEET OF DATA TYPES                  #
#----------------------------------------------------------#
#           NULL - The Value is a null value (NULL)        #
#        INTEGER - The Value is a numeric value (INT)      #
#          REAL - The Value is a float value (FLOAT)       #
#          TEXT - The Value is a text string (STR)         #
#     BLOB - The Value is a blob of data i.e. Binary       #
#           used to store images and files (BYTES)         #
############################################################

conn = sqlite3.connect("bookings.db") #create a connection and specify the database it should connect to
#if that database doesn't exist, it creates it.
cursor = conn.cursor() #create a cursor object using the connection object returned by the connect method
print ("Successfully connected to database")

date = int(input ("please enter a date: "))
rider = str(input ("Please enter the rider name: "))
email = str(input ("Please enter the email address of the rider or rider's guardian: "))
instructor = str(input ("Please enter the instructor's name: "))
lessontype = str(input ("Please enter what type of lesson it is: "))
horse = str(input ("Please enter the horse's name: "))
bookings = int(input ("How many bookings are there: "))
arena = str(input ("What arena is it in: "))

try:
    sqlite_create_table_query = '''CREATE TABLE if not exists table_list(
    date REAL NOT NULL,
    rider TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    instructor TEXT NOT NULL,
    lessontype TEXT NOT NULL,
    horsename TEXT NOT NULL,
    bookings INT NOT NULL,
    arena TEXT NOT NULL);''' #prepares a 'create table' query with columns
    #date format dd.mm.yyyy e.g. 02.11.2009 --- Doesn't work
    cursor.execute(sqlite_create_table_query) #creates the table
    conn.commit() 
    print ("sqlite table created")

    sql_cmd = "SELECT * FROM Project_info WHERE ='{}'".format(Number)
    sqlite_insert_query = '''INSERT INTO table_list * FROM
    (date,rider,email,instructor,lessontype,horsename,bookings,arena)
    VALUES
    ((date), (rider), (email), (instructor), (lessontype), (horse), (bookings), (arena))'''
    count = cursor.execute(sqlite_insert_query)
    conn.commit()
    print ("Information recorded", cursor.rowcount)
    cursor.close() #closes the cursor 

except sqlite3.Error as error: #catch database error
    print ("error:", error) #print error

finally:
    if (conn):
        conn.close() #close SQLite database
        print ("The SQLite connection is closed")
