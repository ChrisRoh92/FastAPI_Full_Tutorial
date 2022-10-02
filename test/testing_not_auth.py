from .testing_main import client


def test_get_all_users_no_auth():
    response = client.get("/users")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}

def test_get_user_by_email_no_auth():
    response = client.get("/user_by_mail?email=test@test.com")
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

def test_change_email():
    pass

def test_change_password():
    pass

def test_delete_user():
    pass

def test_get_all_books_no_auth():
    response = client.get("/books")
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401