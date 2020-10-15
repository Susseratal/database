import sqlite3

try:
    conn = sqlite3.connect("test.db") #create a connection and specify the database it should connect to
    #if that database doesn't exist, it creates it.
    cursor = conn.cursor() #create a cursor object using the connection object returned by the connect method
    print ("Database created successfully")

    sqlite_select_Query = "Select SQLite version;"
    cursor.execute(sqlite_select_Query) #error: No such column
    record = cursor.fetchall()
    print ("SQLite Database Version is: ", record) #prints SQLite database version
    cursor.close #close the cursor opject

except sqlite3.error as error: #catch database error - Ironically error: sqlite3 has no attriubute "error"
    print ("error while connecting to SQLite ", error) #print error

finally:
    if (conn):
        conn.close() #close SQLite database
        print ("The SQLite connection is closed")
