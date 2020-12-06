import datetime
import sqlite3
import sys
from datetime import date
from sqlite3 import Error

def write_data_rider (currentdate: str, rider_firstname: str, rider_surname: str, email: str, riderweight: int, riderage: int, instructor: str, lessontype: str, arena: str) -> bool:
    try:
        sqlite_create_table_query = '''CREATE TABLE if not exists booking(
        currentdate TEXT NOT NULL,
        rider_firstname TEXT NOT NULL,
        rider_surname TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        riderweight INT NOT NULL,
        riderage INT NOT NULL,
        instructor TEXT NOT NULL,
        lessontype TEXT NOT NULL,
        arena TEXT NOT NULL);''' #prepares a 'create table' query with columns
        #date format dd.mm.yyyy e.g. 02.11.2009 --- Doesn't work
        cursor.execute(sqlite_create_table_query) #creates the table
        conn.commit() 
        print ("rider table created")

        sqlite_insert_query = '''INSERT INTO booking
        (currentdate,rider_firstname,rider_surname,email,riderweight,riderage,instructor,lessontype,arena)
        VALUES
        (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        table_row = (currentdate, rider_firstname, rider_surname, email, riderweight, riderage, instructor, lessontype, arena)
        count = cursor.execute(sqlite_insert_query, table_row)
        conn.commit()
        print ("Information recorded", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error: #catch database error
        print ("error:", error) #print error

    finally:
        if (conn):
            conn.close() #close SQLite database
            print ("The SQLite connection is closed")

def write_data_horse (horse_id: int, horse_name: str, horse_weight: int, hours_worked: int) -> bool:
    try:
        sqlite_create_table_query = '''CREATE TABLE if not exists horses(
        horse_id INT NOT NULL,
        horse_name TEXT NOT NULL,
        horse_weight INT NOT NULL
        hours_worked INT NOT NULL);'''
        cursor.execute(sqlite_create_table_query)
        conn.commit()
        print ("horses table created")

        sqlite_insert_query = '''INSERT INTO horses
        (horse_id, horse_name, horse_weight, hours_worked)
        VALUES
        (?, ?, ?, ?)'''
        table_row = (horse_id, horse_name, horse_weight, hours_worked)
        count = cursor.execute(sqlite_insert_query, table_row)
        conn.commit()
        print ("Information recorded", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error: #catch database error
        print ("error:", error) #print error

    finally:
        if (conn):
            conn.close() #close SQLite database
            print ("The SQLite connection is closed")

def take_input_rider():
    print ("User information: ")
    print ("#" * 20)
    currentdate = input ("please enter the date: (format dd/mm/yyyy) ")
    currentdate = datetime.datetime.strptime(currentdate, "%d/%m/%Y").date() #This works but the error handling is atrocious. 
    #Also it doesn't completely work
    currentdate = currentdate.isoformat()
    str(currentdate)
    print (currentdate) #for testing purposes
    rider_firstname = input ("Please enter the rider's first name: ").title()
    rider_surname = input ("Please enter the rider's surname: ").title()
    email = input ("Please enter the email address of the rider or rider's guardian: ")
    riderweight = int(input ("Please enter the weight of the rider in kg: "))
    riderweight = (str(riderweight) + "kg")
    riderage = int(input ("Please enter the age of the rider: "))
    instructor = input ("Please enter the instructor's name: ").title()
    lessontype = input ("Please enter what type of lesson it is: ").title()
    arena = input ("What arena is it in: ").title()
    print ("\nThe data you inputted was: ")
    print ("\nDate: " + str(currentdate))
    print ("\nThe rider's first name: " + rider_firstname)
    print ("\nThe rider's surname: " + rider_surname)
    print ("\nThe email of the rider or rider's guardian: " + email)
    print ("\nThe rider's weight: " + str(riderweight))
    print ("\nThe rider's age: " + str(riderage))
    print ("\nThe lesson instructor: " + instructor)
    print ("\nThe lesson type: " + lessontype)
    print ("\nThe lesson arena: " + arena)
    check = input ("Is this correct? y/n ").lower()
    if check in ["yes", "y"]:
        write_data_rider(currentdate, rider_firstname, rider_surname, email, riderweight, riderage, instructor, lessontype, arena)
        pass

def take_input_horse():
    print ("")
    print ("Horse information: ")
    print ("#" * 20)
    horse_id = int(input ("Please enter the horses ID: "))
    horse_name = input ("Please enter the horse's name: ").title()
    horse_weight = input ("Please enter the horse's wight (in KG): ")
    horse_weight = ((horse_weight) + "kg")
    hours_worked = int(input ("Please enter how many hours the horse has worked: "))
    print ("\nThe data you inputted was: ")
    print ("\nHorse ID: " + str((horse_id)))
    print ("\nHorse name: " + str((horse_name)))
    print ("\nHorse weight: " + str((horse_weight)))
    print ("\nHours worked: " + str((hours_worked)))
    check2 = input ("Is this correct? y/n ").lower()
    if check2 in ["yes", "y"]:
        write_data_horse(horse_id, horse_name, horse_weight, hours_worked)
        pass

