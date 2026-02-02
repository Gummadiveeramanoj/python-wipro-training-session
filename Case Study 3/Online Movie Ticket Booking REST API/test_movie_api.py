import requests

BASE_URL = "http://127.0.0.1:5000"

# Collected Item 1 – Add Movie
movie_payload = {
    "id": 101,
    "movie_name": "Interstellar",
    "language": "English",
    "duration": "2h 49m",
    "price": 250
}

# Collected Item 2 – Update Movie
update_payload = {
    "movie_name": "Interstellar (IMAX)",
    "price": 300
}

# Collected Item 3 – Book Ticket
booking_payload = {
    "movie_id": 101,
    "seats": 2,
    "user_name": "Manu"
}


def test_add_movie():
    response = requests.post(f"{BASE_URL}/api/movies", json=movie_payload)
    assert response.status_code == 201
    assert response.json()["movie_name"] == "Interstellar"


def test_update_movie():
    response = requests.put(f"{BASE_URL}/api/movies/101", json=update_payload)
    assert response.status_code == 200
    assert response.json()["price"] == 300


def test_book_ticket():
    response = requests.post(f"{BASE_URL}/api/bookings", json=booking_payload)
    assert response.status_code == 201
    assert "Booking successful" in response.json()["message"]
