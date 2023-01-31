#import models file
from models import (Base, session, Book, engine)

# Main Menu- add, search, anaylsis, exit, view
# function to add books to the database
# function to edit books
#function to delete them
#Search function
#data cleaning function
#loop thats running the program


if __name__ == "__main__":
    Base.metadata.create_all(engine)