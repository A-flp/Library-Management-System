import getpass
import csv
import sys
import re
import datetime
import time
import os
from tabulate import tabulate

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
current_date = datetime.datetime.now()


def main_menu():

    print(f"""{CYAN}
            /$$       /$$ /$$                                                     /$$$$$$                        /$$
            | $$      |__/| $$                                                    /$$__  $$                      | $$
            | $$       /$$| $$$$$$$   /$$$$$$  /$$$$$$   /$$$$$$  /$$   /$$      | $$  \__/ /$$   /$$  /$$$$$$$ /$$$$$$    /$$$$$$  /$$$$$$/$$$$
            | $$      | $$| $$__  $$ /$$__  $$|____  $$ /$$__  $$| $$  | $$      |  $$$$$$ | $$  | $$ /$$_____/|_  $$_/   /$$__  $$| $$_  $$_  $$
            | $$      | $$| $$  \ $$| $$  \__/ /$$$$$$$| $$  \__/| $$  | $$       \____  $$| $$  | $$|  $$$$$$   | $$    | $$$$$$$$| $$ \ $$ \ $$
            | $$      | $$| $$  | $$| $$      /$$__  $$| $$      | $$  | $$       /$$  \ $$| $$  | $$ \____  $$  | $$ /$$| $$_____/| $$ | $$ | $$
            | $$$$$$$$| $$| $$$$$$$/| $$     |  $$$$$$$| $$      |  $$$$$$$      |  $$$$$$/|  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$ | $$ | $$
            |________/|__/|_______/ |__/      \_______/|__/       \____  $$       \______/  \____  $$|_______/    \___/   \_______/|__/ |__/ |__/
                                                                /$$  | $$                 /$$  | $$
                                                                |  $$$$$$/                |  $$$$$$/
                                                                \______/                  \______/
        """)

    print(f"{GREEN}[1] | Register{RESET}")
    print(f"{YELLOW}[2] | Log-in{RESET}")
    print(f"{CYAN}[3] | See Library Status{RESET}")
    print(f"{RED}[4] | Exit Program{RESET}")
    print("\n")

    try:
        user_input = input("-->> Enter Input [1-4]: ")

        if user_input == '1':
            register()

        elif user_input == '2':
            login()

        elif user_input == '3':
            library_status()

        elif user_input == '4':
            print(f"{CYAN}Goodbye!{RESET}")
            sys.exit()

    except EOFError:
        print(f"{CYAN}Goodbye!{RESET}")
        sys.exit()


def register():

    username_pattern = r"^[A-Za-z]{3,}\w*$"

    print(f"{GREEN}-- Register --{RESET}")

    while True:
        username = input("Username: ")
        username_match = re.fullmatch(username_pattern, username)

        if not username_match:
            print(f"{RED}Invalid Username! 3 alpha characters required first.{RESET}")
        else:
            break

    while True:

        password = getpass.getpass("Enter Password: ")
        confirm_pswd = getpass.getpass("Confirm Password: ")

        if confirm_pswd != password:
            print("Password does not match, try again")
        else:
            break

    print(f"{username} registered successfully at {current_date}")

    with open("people.csv", "a", newline='') as peoplecsv:

        fieldnames = ["username", "password"]
        writer = csv.DictWriter(peoplecsv, fieldnames=fieldnames)

        if os.stat("people.csv").st_size == 0:
            writer.writeheader()

        writer.writerow({
            "username": username,
            "password": password
        })

    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    main_menu()


def login():

    print(f"{YELLOW}-- Username --{RESET}")
    username = input("Input Username: ").strip()
    password = getpass.getpass("Input Password: ").strip()
    try:

        with open("people.csv", 'r', newline='') as peoplecsv:
            reader = csv.DictReader(peoplecsv)

            for row in reader:
                if row["username"].strip() == username and row["password"].strip() == password:
                    library(username)
                    return True

    except FileNotFoundError:
        print("File not Found")
        return False

    print("Invalid Username or Password")
    return False


def library_status():

    with open("books.csv", "r", ) as bookscsv:
                reader = csv.DictReader(bookscsv)
                data = list(reader)

                print(tabulate(data, headers="keys", tablefmt="fancy_grid"))

                acceptance = input("Type Y to go back to the main menu --> ").strip()

                if acceptance == 'y':
                    main_menu()
                else:
                    print(f"{CYAN}Goodbye!{RESET}")
                    sys.exit()

def library(username):

    print(f"""{CYAN}

/$$       /$$ /$$                                                    /$$$$$$$$                                /$$                     /$$
| $$      |__/| $$                                                   |__  $$__/                               |__/                    | $$
| $$       /$$| $$$$$$$   /$$$$$$  /$$$$$$   /$$$$$$  /$$   /$$         | $$  /$$$$$$   /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$ | $$
| $$      | $$| $$__  $$ /$$__  $$|____  $$ /$$__  $$| $$  | $$         | $$ /$$__  $$ /$$__  $$| $$_  $$_  $$| $$| $$__  $$ |____  $$| $$
| $$      | $$| $$  \ $$| $$  \__/ /$$$$$$$| $$  \__/| $$  | $$         | $$| $$$$$$$$| $$  \__/| $$ \ $$ \ $$| $$| $$  \ $$  /$$$$$$$| $$
| $$      | $$| $$  | $$| $$      /$$__  $$| $$      | $$  | $$         | $$| $$_____/| $$      | $$ | $$ | $$| $$| $$  | $$ /$$__  $$| $$
| $$$$$$$$| $$| $$$$$$$/| $$     |  $$$$$$$| $$      |  $$$$$$$         | $$|  $$$$$$$| $$      | $$ | $$ | $$| $$| $$  | $$|  $$$$$$$| $$
|________/|__/|_______/ |__/      \_______/|__/       \____  $$         |__/ \_______/|__/      |__/ |__/ |__/|__/|__/  |__/ \_______/|__/
                                                    /$$  | $$
                                                    |  $$$$$$/
                                                    \______/
        """)

    print(f"{GREEN}[1] | Borrow Books {RESET}")
    print(f"{CYAN}[2] | Return Books {RESET}")
    print(f"{YELLOW}[3] | Back {RESET}")
    print(f"{RED}[4] | Exit Program {RESET}")
    print("\n")

    try:
        user_input = input("-->> Enter Input [1-4]: ")

        if user_input == '1':

            borrow(username)

        elif user_input == '2':

            return_book(username)

        elif user_input == '3':
            main_menu()

        elif user_input == '4':
            print(f"{CYAN}Goodbye!{RESET}")
            sys.exit()

    except EOFError:
        print(f"{CYAN}Goodbye!{RESET}")
        sys.exit()



def borrow(username):

    while True:
        try:
            with open("books.csv", "r") as bookscsv:
                        reader = csv.DictReader(bookscsv)
                        data = list(reader)
                        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))

                        book_to_borrow = input("Enter which book to borrow ( ID ): ")

                        found = False

                        for book in data:


                            if book["ID"] == book_to_borrow:
                                if book["Borrowed by"] == "N/A":
                                    found = True
                                    book["Borrowed by"] = username

                                    with open("books.csv", "w") as bookscsv:

                                        fieldnames = ["ID", "Category", "Details", "Borrowed by"]
                                        writer = csv.DictWriter(bookscsv, fieldnames=fieldnames)

                                        writer.writeheader()
                                        writer.writerows(data)

                                        print(f"{GREEN}Book borrow success!{RESET}")

                                    for i in range(5, 0, -1):
                                        print(i)
                                        time.sleep(1)
                                    library(username)

                                else:
                                    print(f"{RED}-- Someone has already borrowed this book --{RESET}")

                        if not found:
                            print(f"{RED}-- Invalid Book ID! --{RESET}")

                        for i in range(5, 0, -1):
                            print(i)
                            time.sleep(1)
                        library(username)

        except EOFError:
            print(f"{CYAN}Goodbye!{RESET}")
            sys.exit()


def return_book(username):


    while True:
        try:
            with open("books.csv", "r") as bookscsv:
                reader = csv.DictReader(bookscsv)
                books = list(reader)

                borrowed_books = []

                for book in books:
                    if book["Borrowed by"].strip() == username:
                        borrowed_books.append(book)

                if not borrowed_books:
                    print(f"{YELLOW}-- No books to return! --{RESET}")

                    for i in range(5, 0, -1):
                        print(i)
                        time.sleep(1)
                    library(username)


                print(f"{GREEN}-- The followin are the books you borrowed --{RESET}")
                print(tabulate(borrowed_books, headers="keys", tablefmt="fancy_grid"))

                books_to_return = input("Enter which book to return ( ID ): ")

                found = False

                for book in borrowed_books:
                    if book["ID"] == books_to_return:
                        for b in books:
                            if b["ID"] == books_to_return:
                                b["Borrowed by"] = "N/A"
                                found = True
                                break


                if found:
                    with open("books.csv", "w") as bookscsv:

                        fieldnames = ["ID", "Category", "Details", "Borrowed by"]
                        writer = csv.DictWriter(bookscsv, fieldnames=fieldnames)

                        writer.writeheader()
                        writer.writerows(books)
                        print(f"{GREEN}Book return success!{RESET}")
                else:
                    print(f"{RED}Program not properly specified{RESET}")
                    library(username)

        except EOFError:
            print(f"{CYAN}Goodbye!{RESET}")
            sys.exit()

if __name__ == "__main__":
    main_menu()
