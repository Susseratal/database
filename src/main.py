import datetime
import glob
import os
import os.path
import pathlib
import sqlite3
import sys
import time
from datetime import date
from sqlite3 import Error
from secondary import take_input_rider, take_input_horse, show_rider_data, show_horse_data

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
    print("3. Show rider data")
    print("4. Show horse data")
    print("5. Edit a rider's data")
    print("6. Edit a horse's data")
    print("7. Delete a row of data")
    print("8. Show data in the database")
    print("9. Return to the database selection")
    print("10. Show this help message")
    print("11. Quit")
    print("\n")

def main():
    db_path = pathlib.Path(sys.argv[0]).resolve()
    db_path = db_path.parent / ".." / "databases"
    if not db_path.exists():
        db_path.mkdir()
    os.chdir(db_path)
    print("\nCurrent working directory: ")
    print(db_path)

    while True:
        db_connected = False
        while not db_connected:
            file_list = os.listdir(db_path)
            show_help_db()
            db = input("what do you want to do: ").lower()

            if db in ["create database", "1", "add database"]:
                dbname = input("What do you want to call the database: ")
                conn = sqlite3.connect(dbname + ".db") #connect to selected database
                print("successfully created database")
                db_connected = True

            elif db in ["2", "check", "check databases", "check db", "list databases", "list db"]:
                print("Databases: ")
                for file in file_list: 
                    path = pathlib.Path(file)
                    if path.suffix == ".db":
                        print(path.stem) #check the file list for the suffix .db and then prints it without the .db

            elif db in ["3", "connect to database"]:
                print("Databases: ")
                for file in file_list:
                    path = pathlib.Path(file)
                    if path.suffix == ".db":
                        print(path.stem)
                dbname = input("\nWhich database do you want to connect to: ")
                dbname = (dbname + ".db")
                if dbname not in file_list:
                    print ("No such database exists ")
                else:
                    conn = sqlite3.connect(dbname)
                    print("connecting...")
                    time.sleep (0.5)
                    print("Successfully connected to database")
                    db_connected = True

            elif db in ["4", "delete", "delete database"]:
                print("Databases: ")
                for file in file_list:
                    path = pathlib.Path(file)
                    if path.suffix == ".db":
                        print(path.stem)
                print("\nIf you would like to cancel your deletion, just hit return")
                base = input("which database would you like to delete: ")
                dbname = (base + ".db")
                if base in [""]:
                    print("cancelling deletion")
                elif dbname not in file_list:
                    print ("No such database exists ")
                else:
                    print("deleting...")
                    time.sleep(0.5)
                    os.remove (base + ".db")
                    print("Successfully deleted " + base + ".db")

            elif db in ["5", "quit", "exit", "q"]:
                sys.exit()
            else: 
                print("Invalid command")

        print(dbname)
        show_help_table()

        do = input("What would you like to do? ").lower()
        if do in ["add rider", "1"]:
            take_input_rider(conn)
        elif do in ["add horse", "2"]:
            take_input_horse(conn)
        elif do in ["show rider data", "show rider", "3"]:
            show_rider_data(conn)
        elif do in ["show horse data", "show horse", "4"]:
            show_horse_data(conn)
        elif do in ["edit rider", "5"]:
            pass
        elif do in ["edit horse", "6"]:
            pass
        elif do in ["delete row", "delete data", "delete", "7"]:
            print("sorry, that feature doesn't yet exist")
        elif do in ["show row", "show data", "show", "8"]:
            print("sorry, that feature doesn't yet exist")
        elif do in ["return", "return to database list", "database list", "9"]:
            db_connected = False
        elif do in ["help", "10"]:
            show_help_table()
        elif do in ["quit", "11"]:
            sys.exit()
        else:
            print("Invalid command")

if __name__ == '__main__':
    main()
