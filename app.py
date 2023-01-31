#import models file
from models import (Base, session, Book, engine)

import csv
import datetime

# Main Menu- add, search, anaylsis, exit, view

def menu():
    while True:
        print('''
        \nPROGRAMMING BOOKS
        \r1. Add Book
        \r2. View all books
        \r3. Search for book
        \r4. Book Anaylsis
        \r5. Exit
         ''' )
        choice = input("What do you want to do?: ")

        if choice in ['1', '2', '3', '4', '5']:
            return choice

        else:
            input ('''
                  \rPlease choose one of the optins above.
                  \rA number between 1-5.
                  \rpress ENTER to try again.''')




# function to add books to the database
# function to edit books
#function to delete them
#Search function
#data cleaning function
#loop thats running the program

def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 
    'June', 'July', 'August', 'September', 'October', 
    'November', 'December']
    split_date = date_str.split(' ')
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1].replace(",", " "))
    year = int(split_date[2])
    return datetime.date(year, month, day)

def clean_price(price_str):
    price_float = float(price_str)
    price = int(price_float*100)
    return price 


def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            title = row[0]
            author = [1]
            date = clean_date(row[2])
            price = clean_price(row[3])
            new_book = Book( title = title, author = author, 
                           published_date =  date, price = price)
            session.add(new_book)
        session.commit()



def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            #add book
            pass
        elif choice == '2':
            #view all books
            pass
        elif choice == '3':
            #Search for book
            pass
        elif choice == '4':
            #Book Analysis:
            pass
        else: 
            print("Goodbye")
            app_running = False



if __name__ == "__main__":
    Base.metadata.create_all(engine)
    add_csv()
    for book in session.query(Book):
        print(book)