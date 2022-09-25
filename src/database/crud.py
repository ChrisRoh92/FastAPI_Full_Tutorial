from sqlalchemy.orm import Session
from fastapi import HTTPException
## User specific imports
from .models import User, Book, Booking
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
    return db.query(Book).filter_by(author = author).limit(limit).all()

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