import datetime
import sqlite3
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

def write_data (date: str, rider_firstname: str, rider_surname: str, email, instructor: str, lessontype: str, horse: str, bookings: int, arena: str) -> bool:
    conn = sqlite3.connect("bookings.db") #create a connection and specify the database it should connect to
    #if that database doesn't exist, it creates it.
    cursor = conn.cursor() #create a cursor object using the connection object returned by the connect method
    print ("Successfully connected to database")

    try:
        sqlite_create_table_query = '''CREATE TABLE if not exists booking(
        date REAL NOT NULL,
        rider_firstname TEXT NOT NULL,
        rider_surname TEXT NOT NULL,
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

        sqlite_insert_query = '''INSERT INTO booking
        (date,rider_firstname,rider_surname,email,instructor,lessontype,horsename,bookings,arena)
        VALUES
        (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        table_row = (date, rider_firstname, rider_surname, email, instructor, lessontype, horse, bookings, arena)
        count = cursor.execute(sqlite_insert_query, table_row)
        conn.commit()
        print ("Information recorded", cursor.rowcount)
        cursor.close() #closes the cursor 

    except sqlite3.Error as error: #catch database error
        print ("error:", error) #print error

    finally:
        if (conn):
            conn.close() #close SQLite database
            print ("The SQLite connection is closed")

if __name__ == "__main__":
    while True:
        date = input ("please enter a date: (format dd/mm/yyyy) ")
        date = datetime.datetime.strptime(date, "%d/%m/%Y") #This works but the error handling is attrocious. Also it doesn't completely work
        rider_firstname = input ("Please enter the rider's first name: ").title()
        rider_surname = input ("Please enter the rider's surname: ").title()
        email = input ("Please enter the email address of the rider or rider's guardian: ")
        instructor = input ("Please enter the instructor's name: ").title()
        lessontype = input ("Please enter what type of lesson it is: ").title()
        horse = input ("Please enter the horse's name: ").title()
        bookings = int(input ("How many bookings are there: "))
        arena = input ("What arena is it in: ").title()
        print ("\nThe data you inputted was: ")
        print ("\nDate: " + str(date))
        print ("\nThe rider's first name: " + rider_firstname)
        print ("\nThe rider's surname: " + rider_surname)
        print ("\nThe email of the rider or rider's guardian: " + email)
        print ("\nThe lesson instructor: " + instructor)
        print ("\nThe lesson type" + lessontype)
        print ("\nThe horse's name: " + horse)
        print ("\nThe numeber of bookings: " + str(bookings))
        print ("\nThe lesson arena: " + arena)
        check = input ("Is this correct? y/n ").lower()
        if check in ["yes", "y"]:
            break
    write_data(date, rider_firstname, rider_surname, email, instructor, lessontype, horse, bookings, arena)
