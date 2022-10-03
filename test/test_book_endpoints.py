from .prep import client, access_token_header

################################################
## Book specific endpoints:
################################################

## Add Books at first:
def test_add_books():
    input_data = {"title": "Book Title", "author": "Test Author", "isbn" : "123456789"}
    response = client.post("/book/add_single", json=input_data, headers=access_token_header)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['title'] == "Book Title"
    assert response_data['author'] == "Test Author"
    assert response_data['isbn'] == "123456789"

def test_add_same_book_again():
    input_data = {"title": "Book Title", "author": "Test Author", "isbn" : "123456789"}
    response = client.post("/book/add_single", json=input_data, headers=access_token_header)
    assert response.status_code == 404
    response_data = response.json()
    assert response_data == {"detail": "Book with ISBN {} already exist".format("123456789")}

def test_get_book_by_isbn():
    response = client.get("/get_book_by_isbn?isbn=123456789", headers=access_token_header)
    assert response.status_code == 200
    response_data = response.json()
    response_data == {"title": "Book Title", "author": "Test Author", "isbn" : "123456789"}

def test_get_book_by_author():
    ## Use '%20' as space
    response = client.get("/get_books_from_author?author=Test+Author", headers=access_token_header)
    assert response.status_code == 200
    response_data = response.json()
    response_data == {"title": "Book Title", "author": "Test Author", "isbn" : "123456789"}

def test_remove_book_by_isbn():
    ## 1. check if Book is in database:
    response = client.get("/get_book_by_isbn?isbn=123456789", headers=access_token_header)
    assert response.status_code == 200
    response_data = response.json()
    response_data == {"title": "Book Title", "author": "Test Author", "isbn" : "123456789"}

    ## 2. Remove the Book and check delete message
    response = client.delete("/book?isbn=123456789", headers=access_token_header)
    assert response.status_code == 200
    response_data = response.json()
    response_data == {"message": "Book with ISBN {} deleted".format("123456789")}

    ## 3. Check if book is really not in database!
    response = client.get("/get_book_by_isbn?isbn=123456789", headers=access_token_header)
    assert response.status_code == 404
    response_data = response.json()
    response_data == {"detail": "No books with isbn {} found in database".format("123456789")}

def test_add_book_list():
    ## 1. Add a list of books in empty book table
    input_data = { "books": [
                {
                    "title": "Book Title 1",
                    "author": "Test Author",
                    "isbn": "a123456789"
                },
                {
                    "title": "Mathematik für Ingenieure und Naturwissenschaftler Band 2: Ein Lehr- und Arbeitsbuch für das Grundstudium",
                    "author": "Lothar Papula",
                    "isbn": "b123456789"
                },
                {
                    "title": "Mathematische Formelsammlung: Für Ingenieure und Naturwissenschaftler",
                    "author": "Lothar Papula",
                    "isbn": "c123456789"
                }
            ]
        }
    response = client.post("/book/add_list", json=input_data, headers=access_token_header)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data == {"message": "Book upload was successful"}

    ## 2. Get all current books, which should be only the ones, we added in this method:
    new_reponse = client.get("/books", headers=access_token_header)
    assert response.status_code == 200
    new_reponse_data = new_reponse.json()
    ## Need to remove id field, to make comparison more easy
    for element in new_reponse_data:
        del element["id"]

    for book in new_reponse_data:
        assert book in input_data["books"]

def test_update_book_title():
    input_url = "/book_title?new_title={}&isbn={}".format("New+Book+Title", "a123456789")
    response = client.put(input_url, headers=access_token_header)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["isbn"] == "a123456789"
    assert response_data["title"] == "New Book Title"