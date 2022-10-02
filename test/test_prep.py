from fastapi.testclient import TestClient
import pytest
import sys

sys.path.append("..") # Adds higher directory to python modules path.
from app.main import app 

client = TestClient(app)

test_email = "test@test.com"
test_password = "test"
test_fullname = "test"

## Generate Access Token:
def generate_access_token_header(email: str, password: str, fullname:str = test_fullname, is_employee: bool = True):
        data = {"email": email, "password": password, "fullname": test_fullname, "is_employee": is_employee}
        response = client.post("/register", json=data)
        auth_token = response.json()["access_token"]
        return {"Authorization": f"Bearer {auth_token}"}

def update_access_token_header(auth_token: str):
        return {"Authorization": f"Bearer {auth_token}"}

## Added User manually over docs
access_token_header = generate_access_token_header(test_email, test_password)