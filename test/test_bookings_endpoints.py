from .prep import client, access_token_header
from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'
TEST_ISBN   = "F123456789"

################################################
## Booking specific endpoints:
################################################

def test_get_all_bookings_empty():
    response = client.get("/booking/all", headers = access_token_header)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data == []


def test_add_booking():
    ## 1. Add a new Book:
    book_data = {"title": "Booking Tutorial", "author": "Coding With Chris", "isbn": TEST_ISBN}
    book_response = client.post("/book/add_single", json=book_data, headers=access_token_header)
    assert book_response.status_code == 200

    ## 2. Add Booking for new added Book:
    booking_data = {"from_date": "2022-10-03", "to_date": "2022-10-10", "isbn": TEST_ISBN, "description": ""}
    booking_response = client.post("/booking/add", json=booking_data, headers=access_token_header)
    assert booking_response.status_code == 200
    booking_response_data = booking_response.json()
    ## Convert from_date and to_date to utctimestamp
    from_date_timestamp = datetime.strptime("2022-10-03", DATE_FORMAT).timestamp()
    to_date_timestamp   = datetime.strptime("2022-10-10", DATE_FORMAT).timestamp()
    assert booking_response_data["from_timestamp"] == from_date_timestamp
    assert booking_response_data["to_timestamp"] == to_date_timestamp

def test_add_same_booking():
    ## 1. Add Booking for new added Book:
    booking_data = {"from_date": "2022-10-03", "to_date": "2022-10-10", "isbn": TEST_ISBN, "description": ""}
    booking_response = client.post("/booking/add", json=booking_data, headers=access_token_header)
    assert booking_response.status_code == 404
    booking_response_data = booking_response.json()
    assert booking_response_data == {"detail": "Book with ISBN {} is already booked in requested time range".format(TEST_ISBN)}

def test_get_all_bookings():
    ## There should just be one booking, since the 2nd try in 'test_add_same_booking' should not work
    response = client.get("/booking/all", headers=access_token_header)
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) == 1
    single_booking = response_data[0]

    from_date_timestamp = datetime.strptime("2022-10-03", DATE_FORMAT).timestamp()
    to_date_timestamp   = datetime.strptime("2022-10-10", DATE_FORMAT).timestamp()
    assert single_booking["from_timestamp"] == from_date_timestamp
    assert single_booking["to_timestamp"] == to_date_timestamp


def test_get_all_bookings_of_current_user():
    ## There should just be one booking, since the 2nd try in 'test_add_same_booking' should not work
    response = client.get("/booking/user", headers=access_token_header)
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) == 1
    single_booking = response_data[0]

    from_date_timestamp = datetime.strptime("2022-10-03", DATE_FORMAT).timestamp()
    to_date_timestamp   = datetime.strptime("2022-10-10", DATE_FORMAT).timestamp()
    assert single_booking["from_timestamp"] == from_date_timestamp
    assert single_booking["to_timestamp"] == to_date_timestamp

def test_get_all_bookings_of_book_by_isbn():
    ## There should just be one booking, since the 2nd try in 'test_add_same_booking' should not work
    response = client.get("/booking/book_bookings?isbn=F123456789", headers=access_token_header)
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) == 1
    single_booking = response_data[0]

    from_date_timestamp = datetime.strptime("2022-10-03", DATE_FORMAT).timestamp()
    to_date_timestamp   = datetime.strptime("2022-10-10", DATE_FORMAT).timestamp()
    assert single_booking["from_timestamp"] == from_date_timestamp
    assert single_booking["to_timestamp"] == to_date_timestamp
