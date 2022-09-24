from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

## Custom imports:
from .auth.auth_handler import create_access_token, extract_email_from_token, is_token_valid, oauth2_scheme
# database related imports
from .database.database import get_db
from .database.schemas import BookBaseSchema, UserRegisterSchema, BookingBaseSchema, BookBaseListSchema
from .database import crud, models, database


models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

########################################################
## user specific endpoints
########################################################
@app.get("/users", tags=["user"])
def get_all_users(token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    return crud.get_all_users(db)

@app.get("/user_by_mail", tags=["user"])
def get_user_by_mail(token: str = Depends(oauth2_scheme)):
    pass

@app.post("/register", tags=["user"])
def register_user():
    pass

@app.post("/login", tags=["user"])
def login_user():
    ## Will be resolved in next branch
    ## TODO(chrohne): Whats the name of the next branch?
    pass

@app.put("/user/change_email", tags=["user"])
def update_email(new_email: str, token: str = Depends(oauth2_scheme)):
    pass

@app.put("/user/change_pwd", tags=["user"])
def update_password(new_password: str, old_password:str, token: str = Depends(oauth2_scheme)):
    pass

@app.delete("/user", tags=["user"])
def delete_current_user(password: str, token: str = Depends(oauth2_scheme)):
    pass

########################################################
## book specific endpoints
########################################################
@app.get("/books", tags=["book"])
def get_all_books(token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    return crud.get_all_books(db)

@app.get("/books/{isbn}", tags=["book"])
def get_book_by_isbn(isbn:str, token: str = Depends(oauth2_scheme)):
    return {"book isbn": isbn}

@app.get("/books/{author}", tags=["book"])
def get_books_from_author(author: str, token: str = Depends(oauth2_scheme)):
    return {"book author": author} 

@app.post("/book/add_single", tags=["book"])
def add_new_book(book: BookBaseSchema, token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    return crud.add_new_book(db, book)

@app.post("/book/add_list", tags=["book"])
def add_new_books(books: BookBaseListSchema, token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    for book in books.books:
        # print(book)
        crud.add_new_book(db, book)

@app.delete("/book", tags=["book"])
def delete_book_by_isbn(isbn: str, token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    return crud.delete_book_by_isbn(db, isbn)

@app.put("/book_title", tags=["book"])
def update_book_title(new_title: str, isbn: str, token: str = Depends(oauth2_scheme)):
    return {"message": "Title was updated {}".format(new_title)}

########################################################
## booking specific endpoints
########################################################
@app.get("/booking/all", tags=["booking"])
def get_all_bookings(token: str = Depends(oauth2_scheme)):
    pass

@app.get("/booking/user", tags=["booking"])
def get_all_bookings_of_current_user(token: str = Depends(oauth2_scheme)):
    pass

@app.post("/booking/add", tags=["booking"])
def add_single_booking(token: str = Depends(oauth2_scheme)):
    pass

