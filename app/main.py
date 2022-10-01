from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from pydantic import EmailStr

## Custom imports:
from app.auth.auth_handler import create_access_token, extract_email_from_token, is_token_valid, oauth2_scheme, ACCESS_TOKEN_EXPIRE_MINUTES
# database related imports
from app.database.database import get_db
from app.database.schemas import BookBaseSchema, UserRegisterSchema, BookingBaseSchema, BookBaseListSchema
from app.database import crud, models, database


models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

########################################################
## user specific endpoints
########################################################
@app.get("/users", tags=["user"])
def get_all_users(token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    return crud.get_all_users(db)

@app.get("/user_by_mail", tags=["user"])
def get_user_by_mail(email: EmailStr, token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    db_user = crud.get_user_by_mail(db, email)
    if db_user:
        return db_user
    else:
        raise HTTPException(
        status_code=404,
        detail="No User found with {} email".format(email),
        headers={"WWW-Authenticate": "Bearer"},
    )


@app.post("/register", tags=["user"])
def register_user(user: UserRegisterSchema, db = Depends(get_db)):
    if not crud.is_email_already_registered(db, user.email):
        db_user =  crud.register_new_user(db, user)
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        token = create_access_token(data={"email": db_user.email}, expires_delta=access_token_expires)
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(
        status_code=404,
        detail="Email is already in registered!",
        headers={"WWW-Authenticate": "Bearer"},
    )

@app.post("/login", tags=["user"])
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db = Depends(get_db)):
    authenticated = crud.authenticate_user(db, form_data.username, form_data.password)
    if authenticated:
        db_user = crud.get_user_by_mail(db, form_data.username)
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        token = create_access_token(data={"email": db_user.email}, expires_delta=access_token_expires)
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

@app.put("/user/change_email", tags=["user"])
def update_email(new_email: EmailStr, token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    # Get mail from token:
    current_mail = extract_email_from_token(token)
    # Get User from db with current_mail
    db_user = crud.get_user_by_mail(db, current_mail)
    if db_user:
        return crud.update_email(db, db_user, new_email)
    else:
        raise HTTPException(
        status_code=404,
        detail="User does not exist",
        headers={"WWW-Authenticate": "Bearer"},
    )

@app.put("/user/change_pwd", tags=["user"])
def update_password(new_password: str, old_password:str, token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    # Get mail from token:
    current_mail = extract_email_from_token(token)
    authenticated = crud.authenticate_user(db, current_mail, old_password)
    if authenticated:
        # Get User from db with current_mail
        db_user = crud.get_user_by_mail(db, current_mail)
        if db_user:
            return crud.update_password(db, db_user, new_password)
        else:
            raise HTTPException(
                status_code=404,
                detail="User does not exist",
                headers={"WWW-Authenticate": "Bearer"})
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"})

@app.delete("/user", tags=["user"])
def delete_current_user(password: str, token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    # Get mail from token:
    mail = extract_email_from_token(token)
    authenticated = crud.authenticate_user(db, mail, password)
    if authenticated:
        db_user = crud.get_user_by_mail(db, mail)
        if db_user:
            if crud.remove_current_user(db, db_user):
                return {"message": "User with mail {} removed".format(mail)}
            else:
                raise HTTPException(
                            status_code=404,
                            detail="Could not remove current user, please contact admin",
                            headers={"WWW-Authenticate": "Bearer"})
        else:
            raise HTTPException(
                status_code=404,
                detail="Could not remove current user, please contact admin",
                headers={"WWW-Authenticate": "Bearer"})
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"})

########################################################
## book specific endpoints
########################################################
@app.get("/books", tags=["book"])
def get_all_books(token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    return crud.get_all_books(db)

@app.get("/books/{isbn}", tags=["book"])
def get_book_by_isbn(isbn:str, token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    return crud.get_book_by_isbn(db, isbn)

@app.get("/books/{author}", tags=["book"])
def get_books_from_author(author: str, token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    return crud.get_books_from_author(db, author)

@app.post("/book/add_single", tags=["book"])
def add_new_book(book: BookBaseSchema, token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    return crud.add_new_book(db, book)

@app.post("/book/add_list", tags=["book"])
def add_new_books(input_books: BookBaseListSchema, token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    for book in input_books.books:
        crud.add_new_book(db, book)

@app.delete("/book", tags=["book"])
def delete_book_by_isbn(isbn: str, token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    if not crud.delete_book_by_isbn(db, isbn):
        raise HTTPException(
        status_code=404,
        detail="Book with ISBN {} does not exist in database".format(isbn),
        headers={"WWW-Authenticate": "Bearer"},
    )
    else:
        return {"message": "Book with ISBN {} deleted".format(isbn)}

@app.put("/book_title", tags=["book"])
def update_book_title(new_title: str, isbn: str, token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    db_book = crud.get_book_by_isbn(db, isbn)
    if db_book:
        return crud.update_book_title(db, db_book, new_title)
    else:
        raise HTTPException(
        status_code=404,
        detail="Book with ISBN {} does not exist in database".format(isbn),
        headers={"WWW-Authenticate": "Bearer"},
    )

########################################################
## booking specific endpoints
########################################################
@app.get("/booking/all", tags=["booking"])
def get_all_bookings(token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    return crud.get_all_bookings(db)

@app.get("/booking/user", tags=["booking"])
def get_all_bookings_of_current_user(token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    # Get mail from token:
    current_mail = extract_email_from_token(token)
    # Get User from db with current_mail
    db_user = crud.get_user_by_mail(db, current_mail)
    if db_user:
        return crud.get_all_bookings_of_current_user(db, db_user.id)
    else:
        raise HTTPException(
        status_code=404,
        detail="User does not exist",
        headers={"WWW-Authenticate": "Bearer"},
    )

@app.get("/booking/book_bookings", tags=["booking"])
def get_all_bookings_of_a_book_by_isbn(isbn: str, token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    db_book = crud.get_book_by_isbn(db, isbn)
    if db_book:
        return crud.get_all_bookings_of_book(db, db_book.id)
    else:
        raise HTTPException(
                status_code=404,
                detail="Book with ISBN {} does not exist in database".format(isbn),
                headers={"WWW-Authenticate": "Bearer"}
            )

@app.post("/booking/add", tags=["booking"])
def add_single_booking(booking: BookingBaseSchema, token: str = Depends(oauth2_scheme), db = Depends(get_db)):
        # Get mail from token:
    current_mail = extract_email_from_token(token)
    # Get User from db with current_mail
    db_user = crud.get_user_by_mail(db, current_mail)
    if db_user:
        ## Check if requestes Book exist:
        db_book = crud.get_book_by_isbn(db, booking.isbn)
        if db_book:
            if not crud.book_has_booking_in_timerange(db, booking, db_book.id):
                return crud.add_new_booking(db, booking, db_book.id, db_user.id)
            else:
                raise HTTPException(
                status_code=404,
                detail="Book with ISBN {} is already booked in requested time range".format(booking.isbn),
                headers={"WWW-Authenticate": "Bearer"}
            )
        else:
            raise HTTPException(
                status_code=404,
                detail="Book with ISBN {} does not exist in Database".format(booking.isbn),
                headers={"WWW-Authenticate": "Bearer"}
            )
    else:
        raise HTTPException(
        status_code=404,
        detail="User does not exist",
        headers={"WWW-Authenticate": "Bearer"},
    )

