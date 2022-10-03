from sqlalchemy import Date, Time, Column, ForeignKey, Integer, String, Enum, Numeric, Boolean
from sqlalchemy.orm import relationship
from datetime import date, datetime, timedelta
## User specfic imports
from .database import Base

class User(Base):
    __tablename__ = "users"

    id              = Column(Integer, primary_key=True, index=True)
    email           = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_employee     = Column(Boolean)

    bookings        = relationship("Booking", back_populates="user")

class Book(Base):
    __tablename__ = "books"

    id              = Column(Integer, primary_key=True, index=True)
    title           = Column(String, index=True)
    author          = Column(String, index=True)
    isbn            = Column(String, unique=True, index=True)

    bookings     = relationship("Booking", back_populates="booked_book")

class Booking(Base):
    __tablename__ = "bookings"

    id              = Column(Integer, primary_key=True, index=True)
    from_timestamp  = Column(Integer, index=True)
    to_timestamp    = Column(Integer, index=True)
    description     = Column(String, index=True)

    book_id         = Column(Integer, ForeignKey("books.id"))
    booked_book     = relationship("Book", back_populates="bookings")

    user_id         = Column(Integer, ForeignKey("users.id"))
    user            = relationship("User", back_populates="bookings")