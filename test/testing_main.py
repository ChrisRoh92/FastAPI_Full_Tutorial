from fastapi.testclient import TestClient
import pytest
import sys

sys.path.append("..") # Adds higher directory to python modules path.
from app.main import app 

client = TestClient(app)

## Generate Access Token:
def generate_access_token_header(email: str, password: str):
        data = {"email": email, "password": password, "fullname": "string", "is_employee": True}
        response = client.post("/register", json=data)
        auth_token = response.json()["access_token"]
        return {"Authorization": f"Bearer {auth_token}"}

## Added User manually over docs
access_token_header = generate_access_token_header("test@test.com", "test")