#import models file
from models import (Base, session, Book, engine)

import datetime
import csv
import time

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


def submenu():
    while True:
        print('''
        \nEdit Options
        \r1. Edit Book
        \r2. Delete Book
        \r3. Return to main menu ''')
        choice = input("What do you want to do?: ")

        if choice in ['1', '2', '3']:
            return choice

        else:
            input ('''
                  \rPlease choose one of the optins above.
                  \rA number between 1-3.
                  \rpress ENTER to try again.''')

def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 
    'June', 'July', 'August', 'September', 'October', 
    'November', 'December']
    split_date = date_str.split(' ')
    try:
        month = int(months.index(split_date[0]) + 1)
        day = int(split_date[1].split(',')[0])
        year = int(split_date[2])
        return_date = datetime.date(year, month, day)
    
    except ValueError:
        input( ''' 
            \n******** DATE ERROR *********
            \rThe Date format should inlcude a valid Month Day, Year from the past
            \rExample: January 13, 2003
            \rPress ENTER to try again
            \r********************************* ''')
        return

    else:
        return return_date

def clean_price(price_str):
    try:
        price_float = float(price_str)
        price = int(price_float*100)
    except ValueError:
        input( ''' 
            \n******** Price ERROR *********
            \r The Price format should inlcude a decimal point with no special characters
            \rExample: 29.99
            \rPress ENTER to try again
            \r*******************************
            ''')
        return
    else:
        return price 

def clean_id(id_str, options):
    try:
        book_id = int(id_str)
    except:
        input( f''' 
            \n******** Id ERROR *********
            \rId must be a number.
            \rPress ENTER to try again
            \r***************************''')
        return
    else:
        if book_id in options:
            return book_id
        else:
            input( ''' 
            \n******** Id ERROR *********
            \r Options are: {my_options}.
            \rPress ENTER to try again
            \r***************************''')

def edit_check(column_name, current_value):
    print(f'\n**** EDIT {column_name} *****')
    if column_name == 'Price':
        print(f'\nCureent Value: {current_value / 100}' )
    elif column_name == 'Date':
        print(f'\nCurrent Value: {current_value.strftime("%B  %d %Y ")}')
    else:
        print(f'Current Value: {current_value}')
    
    if column_name == 'Date' or column_name == 'Price':
        while True:
            changes = input('What would you like to change the value to?: ')
            if column_name == 'Date':
                changes = clean_date(changes)
                if type(changes) == datetime.date:
                    return changes

            
            elif column_name == 'Price':
                changes = clean_price(changes)
                if type(changes) == int:
                    return changes
    else:
        return input('What would you like to change the value to?: ')



def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            book_in_db = session.query(Book).filter(Book.title ==row[0]).one_or_none()
            if book_in_db == None:
                title = row[0]
                author = row[1]
                date = (clean_date(row[2]))
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
            title = input('Title: ')
            author = input('Author: ')
            date_error = True
            while date_error:
                date = input('Publish Date(Ex: October 25, 2017): ')
                date = clean_date(date)
                if type(date) == datetime.date:
                    date_error = False
            price_error = True
            while price_error:
                price = input ('Price (Example: 29.99): ')
                price = clean_price(price)
                if type(price) == int:
                    price_error = False
            added_book =Book( title = title, author = author, 
                            published_date =  date, price = price)
            session.add(added_book)
            session.commit()
            time.sleep(1.5)
            print('Book Added!')
            time.sleep(1.5)

        elif choice == '2':
            for book in session.query(Book):
                print(f'{book.id} | {book.title} | {book.author}')
            input( "Press ENTER to return to the main menu")
       
        elif choice == '3':
            id_options = []
            for book in session.query(Book):
                id_options.append(book.id)
            id_error = True
            while id_error:
                id_choice = input(f'''
                \nId options: {id_options}
                \rBook id: ''')
                id_choice = clean_id(id_choice, id_options)
                if type(id_choice) == int:
                    id_error = False
            the_book = session.query(Book).filter(Book.id == id_choice).first()
            print(f'''
                  \n{the_book.title} by {the_book.author}
                  \rPublished: {the_book.published_date}
                  \rPrice: $ {the_book.price /100}  
                  \r''')

            sub_choice = submenu()
            if sub_choice == '1':
                 the_book.title == edit_check('Title', the_book.title)
                 the_book.author == edit_check('Author', the_book.author)
                 the_book.published_date == edit_check('Date', the_book.published_date)
                 the_book.price == edit_check('Price', the_book.price)
                 session.commit()
                 time.sleep(1.5)
                 print("Book updated")
                 time.sleep(1.5)
            elif sub_choice == '2':
                session.delete(the_book)
                session.commit()
                time.sleep(1.5)
                print("Book delted")
                time.sleep(1.5)
                pass
            else:
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
    app()
    
    
    