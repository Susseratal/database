import datetime
import os
import os.path
import sqlite3
import sys
from datetime import date
from sqlite3 import Error
from secondary import take_input_rider
from secondary import take_input_horse

##############################################
#     _       _        _                     #
#  __| | __ _| |_ __ _| |__   __ _ ___  ___  #
# / _` |/ _` | __/ _` | '_ \ / _` / __|/ _ \ #
#| (_| | (_| | || (_| | |_) | (_| \__ \  __/ #
# \__,_|\__,_|\__\__,_|_.__/ \__,_|___/\___| #
#                                            #
##############################################

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

def show_help_table():
    print ("\nYou can: ")
    print ("1. Add a rider's data to the database")
    print ("2. Add a horses' data to the database")
    print ("3. Edit data in the database")
    print ("4. Delete a row of data")
    print ("5. Show data in the database")
    print ("6. Return to the database selection")
    print ("7. Show this help message")
    print ("8. Quit")
    print ("\n")

def show_help_db():
    print ("\nYou can: ")
    print ("1. Add a new database")
    print ("2. Connect to an existing database")
    print ("3. Delete a database")
    print ("4. Quit")
    print ("\n")

while True:
    while True:
        show_help_db()
        db = input ("what do you want to do: ")
        if db in ["create database", "1", "add database"]:
            dbname = input ("What do you want to call the database: ")
            conn = sqlite3.connect(dbname + ".db")
            cursor = conn.cursor()
            print ("successfully created database")
            break
        elif db in ["2", "connect to database"]:
            dbname = input ("Which database do you want to connect to: ")
            conn = sqlite3.connect(dbname + ".db")
            cursor = conn.cursor() #create a cursor object using the connection object returned by the connect method
            print ("Successfully connected to database")
            break
        elif db in ["3", "delete", "delete database"]:
            path = "/Users/iainwalker/Programming/GitKraken/database"
            file_list = os.listdir(path)
            if ".db" in file_list(str):
                print ("Databases: ")
                print (file_list)
                base = input ("which database would you like to delete: ")
                os.remove (base + ".db")
            else:
                print ("There are currently no existing databases")
        elif db in ["4", "quit", "exit"]:
            sys.exit()
        else: 
            print ("Invalid command")

    print (dbname)
    show_help_table()
    conn = sqlite3.connect(dbname + ".db") #create a connection and specify the database it should connect to
    cursor = conn.cursor() #create a cursor object using the connection object returned by the connect method
    print ("Sucessfully connected to database")

    do = input ("What would you like to do? ").lower()
    if do in ["add rider", "1"]:
        take_input_rider()
    elif do in ["add horse", "2"]:
        take_input_horse()
    elif do in ["return", "return to database list", "database list", "6"]:
        continue
    elif do in ["help", "7"]:
        show_help_table()
    elif do in ["quit", "8"]:
        sys.exit()
    else:
        print ("Invalid command")
