import sqlite3

try:
    conn = sqlite3.connect("test.db") #create a connection and specify the database it should connect to
    #if that database doesn't exist, it creates it.
    sqlite_create_table_query = '''CREATE TABLE table_list(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email text NOT NULL UNIQUE);''' #prepares a 'create table' query with columns

    cursor = conn.cursor() #create a cursor object using the connection object returned by the connect method
    print ("Database created successfully")
    cursor.execute(sqlite_create_table_query) #creates the table
    conn.commit() 
    print ("sqlite table created")

    cursor.close() #close the cursor

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
