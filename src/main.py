from fastapi import FastAPI

app = FastAPI()

########################################################
## user specific endpoints
########################################################
@app.get("/users", tags=["user"])
def get_all_users():
    pass

@app.get("/user_by_mail", tags=["user"])
def get_user_by_mail():
    pass

@app.post("/register", tags=["user"])
def register_user():
    pass

@app.post("/login", tags=["user"])
def login_user():
    pass

@app.put("/user/change_email", tags=["user"])
def update_email():
    pass

@app.put("/user/change_pwd", tags=["user"])
def update_password():
    pass

@app.delete("/user", tags=["user"])
def delete_current_user():
    pass

########################################################
## book specific endpoints
########################################################
@app.get("/books", tags=["book"])
def get_all_books():
    pass

@app.get("/books/{isbn}", tags=["book"])
def get_book_by_isbn(isbn:str):
    return {"book isbn": isbn}

@app.get("/books_by_author", tags=["book"])
def get_book_by_author(author: str):
    return {"book author": author} 

@app.post("/book", tags=["book"])
def add_new_book(title: str, author: str, isbn: str):
    return {"title": title, "author": author, "isbn": isbn}

@app.delete("/book", tags=["book"])
def delete_book_by_isbn(isbn: str):
    pass

@app.put("/book_title", tags=["book"])
def update_book_title(new_title: str, isbn: str):
    return {"message": "Title was updated {}".format(new_title)}

########################################################
## booking specific endpoints
########################################################
@app.get("/booking/all", tags=["booking"])
def get_all_bookings():
    pass

@app.get("/booking/user", tags=["booking"])
def get_all_bookings_of_current_user():
    pass

@app.post("/booking/add", tags=["booking"])
def add_single_booking():
    pass

