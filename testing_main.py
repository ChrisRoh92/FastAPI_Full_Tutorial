from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_get_all_users():
    response = client.get("/users")
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

def test_get_user_by_email():
    response = client.get("/user_by_mail")
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401

def test_get_all_books():
    response = client.get("/books")
    assert response.json() == {"detail": "Not authenticated"}
    assert response.status_code == 401