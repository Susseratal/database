
Database README

<!-- language: lang-none -->
             _       _        _                    
          __| | __ _| |_ __ _| |__   __ _ ___  ___ 
         / _` |/ _` | __/ _` | '_ \ / _` / __|/ _ \
        | (_| | (_| | || (_| | |_) | (_| \__ \  __/
         \__,_|\__,_|\__\__,_|_.__/ \__,_|___/\_ _|

This is an open source database. This is sort of a demonstration to prove that you don't need an overcomplicated interface for something like this.

I appreciate that most databases are now on web portals or something similar, but  
A: I am one of the three people left in the world who says that storing everything on the internet is stupid  
B: It's designed to run on a Windows XP machine with processing power that would make someone from the Napoleonic war laugh  
C: It's designed to run on a Windows XP machine with no internet connection.

Changelog:

        - [x] Downloaded DB browser for SQLite. Seems like it'll be useful
        - [x] Created demo file. Still doesn't work, but I'm getting there with the docs
        - [x] Demo file now works
        - [x] Added file type cheat sheet with python versions
        - [x] Added requriements file which isn't what it looks like. It's what the program is required to do. Should change
        - [x] I've got the structure and workflow clearer in my head (and on a napkin in the coffee shop I'm sat in)
        - [x] Added calendar.py to learn the calendar system
        - [x] deleted calendar.py and just started doing it in main.py
        - [x] I think I've broken it
        - [x] I made what should actually have been the requirements file and it's completely empty. Apparently this program doesn't require anything.
        - [x] why must I break everything I touch?
        - [x] Added License
        - [x] Created user input functionality
        - [x] Allow users to edit data in case they need to change something
        - [x] Change the case of certain inputs so it repairs capitalisation for them
        - [x] Make the date feature have some fancy datetime formatting
        - [x] Reformat to have a function (using code from Alex's fork)
        - [x] Fix the date feature so that it has the correct formatting because it's still broken as hell
        - [x] Datetime input sanitisation and better error handling
        - [x] Added rider weight and rider age inputs
        - [x] Add horse weight and age inputs
        - [x] Add hours worked so that horses can't be overworked
        - [x] WHY DOES IT SAY THERE IS NO SQLITE MODULE I AM BAFFLED?!? (the module is called sqlite3 not sqlite)
        - [x] Email (input field) failed now? Perhaps it's fine? Watch this.
        - [x] Generate horses table
        - [x] Fixed everything that was very broken so it works again :)
        - [x] Create function to generate a database with a custom name
        - [x] Trying to create custom databases (conn not defined in secondary)
        - [x] Added ability to break out of main loop to go back to database selection
        - [x] Fix "no databases" bug
        - [x] Can jump in and out of databases
        - [x] Check list of databases
        - [x] Can delete databases but no error handling so if db doesn't exist, it crashes
        - [x] Added a couple of UX improvements to make workflow more pleasant
        - [x] Organise file structure so databases are in "databases" folder
        - [x] NO SPACES
        - [x] sys.argv so it doesn't matter where script runs from the path doesn't break (used pathlib)
        - [x] Cope with missing databases directory
        - [x] When connecting to and deleting databases show db names without.db
        - [x] Error handling for deleting databases (last time it just printed the error message a few times in the "no databases" bug)
        - [x] (no longer) Need to quit out and reload program in order to register a newly created database. (bad workflow must fix)
        - [x] Need to be able to add rows of data without crash (conn is not defined) ## I am avoiding this problem ## my enemy is defeated
        - [x] deleting databases is broken again (I fixed it)
        - [x] Print rows of data in the program so you don't have to open DBBrowser each time

To Do:

        - [ ] After doing anything it kicks you back to database selection, should fix
        - [ ] Correct formatting on printing data
        - [ ] Add ability to edit and delete rows of data
        - [ ] Deleting databases using integers (like notes in frank)
        - [ ] generate "Horses" table with primary key, foreign key and auto increment
        - [ ] Calculate if a rider and horse are compatable
        - [ ] datetime formatting has no error handling/exceptions
        - [ ] Rework menu system to avoid repetition (function to show menu and prompt for input)
        - [ ] Just do it all again from scratch
        - [ ] Use curses for the interface perhaps?
