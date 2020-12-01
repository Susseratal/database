import datetime
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

def show_help():
    print ("You can: ")
    print ("\n1. Add a rider's data to the database")
    print ("\n2. Add a horses' data to the database")
    print ("\n3. Edit data in the database")
    print ("\n4. Delete a row of data")
    print ("\n5. Show data in the database")
    print ("\n6. Show this help message")
    print ("\n7. Quit")
    print ("\n")

show_help()

while True:
    do = input ("What would you like to do? ").lower()
    if do in ["add rider", "1"]:
        take_input_rider()
    elif do in ["add horse", "2"]:
        take_input_horse()
    elif do in ["help", "6"]:
        show_help()
    elif do in ["quit", "7"]:
        sys.exit()
    else:
        print ("Invalid command")
