# Library Management System ( CLI-Based )

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)

![Status](https://img.shields.io/badge/Status-Completed-green)

![edX](https://img.shields.io/badge/CS50-Python-blueviolet?logo=edx&logoColor=white)

![edX](https://img.shields.io/badge/Final-Project-blueviolet?logo=edx&logoColor=white)


## Overview

### A library management system built with python. It features the ability to allow users to register with their names and password, log-in, see current library details for skimming, and return/borrow books from the library. Also features color changing texts to make it presentable and easy to read. (Similar to the colored syntax when coding)

## Requirements

### Built-in to python:

- ### ***getpass***
- ### ***csv***
- ### ***sys***
- ### ***re***
- ### ***datetime***
- ### ***time***
- ### ***os***

### Pip-installable:

- ### ***Tabulate***

## Main Functions

### This program contains 7 functions, with 6 outside of the main function named "main_menu()"

- ### main_menu()

       Is the main function of this program, apologies for not calling it literally 'main'.

       Starts by welcome the user with an ASCII text which acts as the "header" or "title" of the program

       prompts the user for inputs from 1-4 (str) then depending on the user's input, calls the respective functions for each str number.

       1 calls register() function
       2 calls login() function
       3 calls library_status() function
       4 exits the program with sys.exit

       supports program termination via control + d input with Exception EOFError line 56-58

- ### register()

    #### Overview

       Handles user desire to create their profile in order to properly borrow and return books.


    #### username validation

       For validation of user's name, regex r"^[A-Za-z]{3,}\w*$" is implemented which makes sure that the users type 3 alpha characters first ( to avoid users typing 123 as their names we dont wan't that.)

       uses a while true loop so incase the user keeps typing invalid names the program just reprompts.

    #### password validation

        Uses getpass library to validate user password input. prevents user from seeing what password they are typing to avoid others "peeking".

        Additionally, after the user is prompted for their initial password, they are reprompted again to confirm their password. if the users initial password doesn't equal their initial password, the user will start over.

        once the user is successful, they are broken out of the while true loop and the program starts their username and password in the people.csv file in the root folder of the program

    #### Writing the details

        uses csv's built in function named DictWriter to write the details on the program.
        uses os validation to check if the people.csv = 0 byte. if equal then write header, if not then proceed to write details.

        after writing, wait 5 second, calls main_menu() to allow the user to login

- ### login()

    #### Overview

        Prompts the user for their name and password. the program then checks if the user's name and password is in the people.csv file, call library() which is the function that allows the user to borrow/return books

        also passes user inputted username to library for borrowing and returning books.


        if people.csv or users name and password is invalid, return false

- ### library_status()

    #### Overview

        more of a utility than functionality, just allows the user to see the status of books

                ___________________________________
                | ID | Details      | Borrowed By |
                | 12 | History BOOK | Username    |
               ------------------------------------

        like this ( the quality from the program is better than this )

- ### library(username)

    #### Overview

        Second main function aside from main_menu()

        prints a welcome text like main_menu()

        Prompts the user for input from 1-4

        1 calls borrow(username) function for borrowing books
        2 calls return_book(username) function for returning books
        3 calls back which just returns the user to main_menu()
        4 initiates sys.exit

- ### library(username)

    #### Overview

        Second main function aside from main_menu()

        prints a welcome text like main_menu()

        Prompts the user for input from 1-4

        1 calls borrow(username) function for borrowing books
        2 calls return_book(username) function for returning books
        3 calls back which just returns the user to main_menu()
        4 initiates sys.exit

- ### borrow(username)

    #### Overview

         Prompts the user to choose which book to borrow from the library table.

        Checks if the book is already borrowed:

        - If not, assigns the book to the username in the `Borrowed by` column of `books.csv`
        - If yes, displays an error message

        After successful borrowing, waits 5 seconds and returns to `library(username)`.

- ### borrow(username)

    #### Overview

        Displays all books currently borrowed by the user.

        Prompts the user to select which book to return.

        Updates the `Borrowed by` column in `books.csv` to `N/A` for returned books.

        Handles errors if the user has no borrowed books or enters an invalid book ID.

        After successful return, displays a confirmation and returns to `library(username)`.

- ### TODO

    #### Integrate a notification system that'll check if all books are occupied by checking whether or not column in row Borrowed by is not marked N/A. if true, in the main_menu() print something like All books borrowed in red text else print number of books available.
