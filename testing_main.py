from fastapi.testclient import TestClient
import pytest

from app.main import app

client = TestClient(app)

class TestFastAPI():
    

    def get_token_by_register():
        data = {
            "email": "pytest@test.de",
            "password": "test",
            "fullname": "test test",
            "is_employee": True}

        response = client.post(
        "/register",
        json=data,
        )
        assert response.status_code == 200
        assert response.json() != {"detail": "Email is already in registered!"}
        auth_token = response.json()["access_token"]
        return {"Authorization": f"Bearer {auth_token}"}

    headers = get_token_by_register()

    
    
    def test_get_all_users_no_auth(self):
        response = client.get("/users")
        assert response.json() == {"detail": "Not authenticated"}
        assert response.status_code == 401

    def test_get_all_users_with_token(self):
        response = client.get("/users", headers=self.headers)
        assert response.status_code == 200
        assert response.json() == {"detail": "Not authenticated"}
        

    def test_get_user_by_email_no_auth(self):
        response = client.get("/user_by_mail")
        assert response.json() == {"detail": "Not authenticated"}
        assert response.status_code == 401

    def test_get_all_books_no_auth(self):
        response = client.get("/books")
        assert response.json() == {"detail": "Not authenticated"}
        assert response.status_code == 401