import datetime
import glob
import os
import os.path
import sqlite3
import sys
import time
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

def show_help_db():
    print("\nYou can: ")
    print("1. Add a new database")
    print("2. List existing databases")
    print("3. Connect to an existing database")
    print("4. Delete a database")
    print("5. Quit")
    print("\n")

def show_help_table():
    print("\nYou can: ")
    print("1. Add a rider's data to the database")
    print("2. Add a horses' data to the database")
    print("3. Edit data in the database")
    print("4. Delete a row of data")
    print("5. Show data in the database")
    print("6. Return to the database selection")
    print("7. Show this help message")
    print("8. Quit")
    print("\n")

os.chdir ("databases")
path = (os.getcwd())
file_list = os.listdir(path)
os.path.join (path, "")
print("\nCurrent working directory: ")
print(path + "/" + sys.argv[0])

while True:
    while True:
        show_help_db()
        db = input("what do you want to do: ").lower()
        if db in ["create database", "1", "add database"]:
            dbname = input("What do you want to call the database: ")
            conn = sqlite3.connect(dbname + ".db")
            cursor = conn.cursor()
            print("successfully created database")
            break
        elif db in ["2", "check", "check databases", "check db", "list databases", "list db"]:
            print("Databases: ")
            for file in file_list:
                if file.endswith (".db"):
                    print(os.path.join(file))
        elif db in ["3", "connect to database"]:
            print("Databases: ")
            for file in file_list:
                if file.endswith (".db"):
                    print(os.path.join(file))
            dbname = input("Which database do you want to connect to: ")
            dbname = (dbname + ".db")
            if dbname not in file_list:
                print ("No such database exists ")
            else:
                conn = sqlite3.connect(dbname + ".db")
                cursor = conn.cursor() #create a cursor object using the connection object returned by the connect method
                print("connecting...")
                time.sleep (0.5)
                print("Successfully connected to database")
                break
        elif db in ["4", "delete", "delete database"]:
            print("Databases: ")
            for file in file_list:
                if file.endswith (".db"):
                    print(os.path.join(file))
                    print("If you would like to cancel your deletion, just type any of 'c, escape, cancel' and hit return")
                    base = input("which database would you like to delete: ")
                    if base in ["cancel", "c", "escape"]:
                        print("cancelling deletion")
                        break
                    else:
                        print("deleting...")
                        time.sleep(0.5)
                        os.remove (base + ".db")
                        print("Successfully deleted " + base + ".db")
                        break
        elif db in ["5", "quit", "exit", "q"]:
            sys.exit()
        else: 
            print("Invalid command")

    print(dbname)
    show_help_table()

    do = input("What would you like to do? ").lower()
    if do in ["add rider", "1"]:
        take_input_rider()
    elif do in ["add horse", "2"]:
        take_input_horse()
    elif do in ["edit", "edit row", "edit data", "3"]:
        print("sorry, that feature doesn't yet exist")
    elif do in ["delete row", "delete data", "delete", "4"]:
        print("sorry, that feature doesn't yet exist")
    elif do in ["show row", "show data", "show", "5"]:
        print("sorry, that feature doesn't yet exist")
    elif do in ["return", "return to database list", "database list", "6"]:
        continue
    elif do in ["help", "7"]:
        show_help_table()
    elif do in ["quit", "8"]:
        sys.exit()
    else:
        print("Invalid command")
