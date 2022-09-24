from sqlalchemy.orm import Session
## User specific imports
from .models import User, Book, Booking
from .schemas import UserRegisterSchema, BookBaseSchema, BookingBaseSchema

########################################################
## user specific methods
########################################################
def get_all_users(db: Session, limit: int = 100):
    return db.query(User).all()

def get_user_by_mail(db: Session, email_query: str):
    return db.query(User).filter_by(email = email_query).first()

def register_new_user(db: Session, new_user: UserRegisterSchema):
    pass ## TODO(chrohne)

def update_password(db: Session, db_user:User, new_password:str):
    pass ## TODO(chrohne)

def update_email(db: Session, db_user:User, new_email:str):
    db_user.email = new_email
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def remove_current_user(db: Session, db_user: User):
    db.query(User).filter_by(id = db_user.id).delete()
    db.commit()
    return {"message": "User with email {} was remove".format(db_user.email)}

########################################################
## book specific methods
########################################################
def get_all_books(db: Session, limit: int = 100):
    return db.query(Book).limit(limit).all()

def get_book_by_isbn(db: Session, isbn: str):
    return db.query(Book).filter_by(isbn = isbn).first()

def get_books_from_author(db: Session, author: str, limit: int = 100):
    return db.query(Book).filter_by(author = author).limit(limit).all()

def get_books_with_title_contains_query(db: Session, query: str):
    pass ## TODO(chrohne): Check how to implement!

def delete_book_by_isbn(db: Session, isbn: str):
    db.query(Book).filter_by(isbn = isbn).delete()
    db.commit()
    return {"message": "Book with isbn {} removed".format(isbn)}

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