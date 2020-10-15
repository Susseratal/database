import sqlite3
import datetime
import calendar

#############################################################################################
#                                   CALENDAR STUFF                                          #
#############################################################################################

#class calendar.Calendar(firstweekday = 0)


#############################################################################################
#                                   DATABASE STUFF                                          #
#############################################################################################

try:
    conn = sqlite3.connect("bookings.db") #create a connection and specify the database it should connect to
    #if that database doesn't exist, it creates it.
    cursor = conn.cursor() #create a cursor object using the connection object returned by the connect method
    print ("Successfully connected to database")

    sqlite_create_table_query = '''CREATE TABLE table_list(
    date REAL NOT NULL,
    rider TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    instructor TEXT NOT NULL,
    lessontype TEXT NOT NULL,
    horsename TEXT NOT NULL,
    bookings INT NOT NULL,
    arena TEXT NOT NULL);''' #prepares a 'create table' query with columns
    #date format dd.mm.yyyy e.g. 02.11.2009
    cursor.execute(sqlite_create_table_query) #creates the table
    conn.commit() 
    print ("sqlite table created")
    cursor.close() #close the cursor
    
    sqlite_insert_query = '''INSERT INTO table_list
    (date,rider,email,instructor,lessontype,horsename,bookings,arena)
    VALUES
    (17082020, "John Smith", "demo@address.com", "Becky", "Practice", "Mental", 1, "indoors")'''
    count = cursor.execute(sqlite_insert_query)
    conn.commit()
    print ("Information recorded", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error: #catch database error
    print ("error:", error) #print error

finally:
    if (conn):
        conn.close() #close SQLite database
        print ("The SQLite connection is closed")


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
