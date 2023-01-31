#create a database
from sqlalchemy import (create_engine, Column, 
                        String, Integer, Date)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#create a model
engine = create_engine('sqlite:///books.db', echo = False)
Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()


#books.db
#title, author, date, price

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key= True)
    title = Column('Title', String)
    author = Column('Author', String)
    published_date = Column('Published', Date)
    price = Column('Price', Integer)

    def __repr__(self):
        return f'Title: {self.title} Author: {self.author} Published:{self.published_date} Price: {self.price}'


