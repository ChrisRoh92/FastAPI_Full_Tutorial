from .test_prep import client

'''
All tests in this file should ensure, that no endpoint which need a token, return data, withoud
providing a token
'''

################################################
## User specific endpoints:
################################################
def test_get_all_users_no_auth():
    response = client.get("/users")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}

def test_get_user_by_email_no_auth():
    response = client.get("/user_by_mail?email=test@test.com")
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

def test_change_email_no_auth():
    response = client.put("/user/change_email", json={"new_email" : "a@a.de"})
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

def test_change_password_no_auth():
    response = client.put("/user/change_email", json={"new_password " : "new_test", "old_password" : "test"})
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

def test_delete_user_no_auth():
    response = client.delete("/user", json={"password" : "test"})
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

################################################
## Book specific endpoints:
################################################

def test_get_all_books_no_auth():
    response = client.get("/books")
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

def test_get_book_by_isbn_no_auth():
    response = client.get("/books", json={"isbn":"xxxxxx"})
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

def test_get_book_by_author_no_auth():
    response = client.get("/books", json={"author":"test author"})
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

def test_add_single_book_no_auth():
    input_data = {"title": "Test", "author": "author test", "isbn": "xxxxxxxxx"}
    response = client.post("/book/add_single", json=input_data)
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

def test_add_book_list_no_auth():
    input_data = {
        "books": [
            {"title": "Test", "author": "author test", "isbn": "xxxxxxxxx"},
            {"title": "Test1", "author": "author test", "isbn": "xxxxxxxxx"},
            {"title": "Test2", "author": "author test", "isbn": "xxxxxxxxx"},
            {"title": "Test3", "author": "author test", "isbn": "xxxxxxxxx"},
        ]
    }        
    response = client.post("/book/add_single", json=input_data)
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

def test_delete_book_by_isbn_no_auth():
    response = client.delete("/book", json={"isbn": "xxxxx"})
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

def test_update_book_title_no_auth():
    response = client.put("/book_title", json={"new_tile": "New Book Title", "isbn" : "xxxxxx"})
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

################################################
## Book specific endpoints:
################################################

def test_get_all_bookings_no_auth():
    response = client.get("/booking/all")
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

def test_get_all_bookings_from_current_user_no_auth():
    response = client.get("/booking/user")
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

def test_get_all_bookings_from_book_no_auth():
    response = client.get("/booking/book_bookings")
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

def test_add_new_booking():
    input_data = {"from_date": "2022-10-02", "to_date": "2022-10-02", "isbn": "xxxxx", "description": "some extra description"}
    response = client.post("/booking/add", json=input_data)
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401