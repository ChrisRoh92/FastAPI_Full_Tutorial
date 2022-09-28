from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 202
    assert response.json() == {"msg": "Hello World"}

# def test_read_register():
#     # response = client.post(
#     #     "/register",
#     #     headers={"X-Token": "coneofsilence"},
#     #     json={
#     #         "email": "user@example.com",
#     #         "password": "string",
#     #         "fullname": "string",
#     #         "is_employee": True
#     #         },

#     # )
#     assert 200 == 200