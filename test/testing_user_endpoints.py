from .test_prep import client, access_token_header, test_email, test_password, test_fullname, update_access_token_header

#################################################
## Test user specific endpoints with auth token
#################################################

def test_get_all_users_with_auth():
    response = client.get("/users", headers=access_token_header)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data[0]['email'] == test_email
    assert response_data[0]['is_employee'] == True

def test_get_all_by_email_with_auth():
    input_url = "/user_by_mail?email={}".format(test_email)
    response = client.get(input_url, headers=access_token_header)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['email'] == test_email
    assert response_data['is_employee'] == True

def test_register_same_user():
    data = {"email": test_email, "password": test_password, "fullname": test_fullname, "is_employee": True}
    response = client.post("/register", json=data)
    response_data = response.json()
    assert response.status_code == 404
    assert response_data == {"detail": "Email is already in registered!"}

def test_login_user():
    input_data = {"grant_type": "", "username": test_email, "password": test_password, "scope" : "", "client_id" : "", "client_secret" : ""}
    response = client.post("/login", data= input_data)
    response_data = response.json()
    assert response.status_code == 200
    assert "access_token" in response_data

def test_update_email_with_auth():
    response = client.put("/user/change_email?new_email=a@a.de", headers=access_token_header)
    response_data = response.json()
    assert response.status_code == 200
    print(response_data)
    global new_access_token_header
    ## Because we use the token to extract the email, we need to refresh the token, because we changed
    # the email of the database user
    auth_token = response_data["access_token"]
    new_access_token_header = update_access_token_header(auth_token)

def test_update_password_with_auth():
    input_url = "/user/change_pwd?new_password=new_test&old_password={}".format(test_password)
    response = client.put(input_url, headers=new_access_token_header)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['email'] == "a@a.de"
    assert response_data['is_employee'] == True

def test_delete_current_user():
    response = client.delete("/user?password=new_test", headers=new_access_token_header)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data == {"message": "User with mail a@a.de removed"}
    ## Token should for now be usable anyway, so lets check if user still exists:
    input_url = "/user_by_mail?email={}".format("a@a.de")
    new_response = client.get(input_url, headers=access_token_header)
    assert new_response.status_code == 404
    new_response_data = new_response.json()
    assert new_response_data == {"detail": "No User found with a@a.de email"}
