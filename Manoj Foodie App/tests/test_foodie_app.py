import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"

def test_register_restaurant():
    response = requests.post(
        f"{BASE_URL}/restaurants",
        json={
            "name": "Food Hub",
            "category": "Indian",
            "location": "Hyderabad"
        }
    )
    assert response.status_code == 201


def test_register_duplicate_restaurant():
    response = requests.post(
        f"{BASE_URL}/restaurants",
        json={"name": "Food Hub"}
    )
    assert response.status_code == 409


def test_register_user():
    response = requests.post(
        f"{BASE_URL}/users/register",
        json={
            "name": "Manu",
            "email": "manu@gmail.com"
        }
    )
    assert response.status_code == 201


def test_place_order():
    response = requests.post(
        f"{BASE_URL}/orders",
        json={
            "user_id": "sample-user",
            "restaurant_id": "sample-restaurant",
            "dishes": ["Pizza", "Burger"]
        }
    )
    assert response.status_code == 201
