from sqlalchemy.orm import Session
from fastapi import HTTPException
<<<<<<< HEAD
from sqlalchemy import or_, and_
=======
>>>>>>> bc2a4ab (Add Method to hash password for user, register/login/update password/email)
## User specific imports
from .models import User, Book, Booking
from .utils import create_timestamp
from .schemas import UserRegisterSchema, BookBaseSchema, BookingBaseSchema
from ..auth.password_handler import verify_password, get_password_hash

########################################################
## user specific methods
########################################################
def get_all_users(db: Session, limit: int = 100):
    return db.query(User).all()

def get_user_by_mail(db: Session, email_query: str):
    return db.query(User).filter_by(email = email_query).first()

def register_new_user(db: Session, new_user: UserRegisterSchema):
    hashed_password = get_password_hash(new_user.password)
    db_user = User(
        email=(new_user.email).lower(),
        hashed_password=hashed_password,
        is_employee=new_user.is_employee)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def is_email_already_registered(db: Session, email: str):
    db_user = get_user_by_mail(db, email)
    if db_user:
        return True
    else:
        return False

def authenticate_user(db: Session, email: str, password:str):
    db_user = get_user_by_mail(db, email)
    if not db_user:
        return False
    return verify_password(password, db_user.hashed_password)

def update_password(db: Session, db_user:User, new_password:str):
    hashed_password = get_password_hash(new_password)
    db_user.hashed_password = hashed_password
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_email(db: Session, db_user:User, new_email:str):
    db_user.email = new_email
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def remove_current_user(db: Session, db_user: User):
    successful = db.query(User).filter_by(id = db_user.id).delete()
    if successful:
        db.commit()
        return True
    else:
        return False

########################################################
## book specific methods
########################################################
def get_all_books(db: Session, limit: int = 100):
    return db.query(Book).limit(limit).all()

def get_book_by_isbn(db: Session, isbn: str):
    return db.query(Book).filter_by(isbn = isbn).first()

def get_books_from_author(db: Session, author: str, limit: int = 100):
    return db.query(Book).filter_by(author = author).all()

def delete_book_by_isbn(db: Session, isbn: str):
    successful = db.query(Book).filter_by(isbn = isbn).delete()
    if successful:
        db.commit()
        return True
    else:
        return False
        
def add_new_book(db: Session, book: BookBaseSchema):
    db_book = Book(
        title = book.title,
        author = book.author,
        isbn = book.isbn
    )
    db.add(db_book)
    db.flush()
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book_title(db: Session, db_book: Book, new_title: str):
    db_book.title = new_title
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def does_book_exist(db: Session, isbn:str):
    db_book =  db.query(Book).filter_by(isbn = isbn).first()
    if db_book:
        return True
    return False

########################################################
## booking specific methods
########################################################
def get_all_bookings(db: Session, limit: int = 100):
    return db.query(Booking).all()

def book_has_booking_in_timerange(db: Session, booking: BookingBaseSchema, book_id: int):
    from_timestamp = create_timestamp(booking.from_date)
    to_timestamp = create_timestamp(booking.to_date)

    if to_timestamp - from_timestamp < 0.0:
        raise HTTPException(status_code=404, detail= "End Date and Time is before start Date and Time")

    cond1 = and_(to_timestamp >= Booking.from_timestamp, to_timestamp < Booking.to_timestamp)
    cond2 = and_(from_timestamp >= Booking.from_timestamp, from_timestamp < Booking.to_timestamp)

    bookings = db.query(Booking).filter_by(book_id = book_id).filter(or_(cond1, cond2)).all()
    if bookings:
        print(bookings)
        return True
    return False

def get_all_bookings_of_current_user(db: Session, user_id: int):
    return db.query(Booking).filter_by(user_id = user_id).all()

def get_all_bookings_of_book(db: Session, book_id: int):
    # Get Book id:
    return db.query(Booking).filter_by(book_id = book_id).all()


def add_new_booking(db: Session, booking: BookingBaseSchema, book_id: int, user_id: int):
    db_booking = Booking(
        from_timestamp = create_timestamp(booking.from_date),
        to_timestamp = create_timestamp(booking.to_date),
        description = booking.description,
        book_id = book_id,
        user_id = user_id
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking
