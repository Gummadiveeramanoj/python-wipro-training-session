import requests

BASE_URL = "http://127.0.0.1:5000/api"

def test_add_patient():
    payload = {
        "name": "John",
        "age": 30,
        "gender": "Male",
        "contact": "9999999999",
        "disease": "Fever",
        "doctor": "Dr. Smith"
    }
    response = requests.post(f"{BASE_URL}/patients", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "John"

def test_get_patients():
    response = requests.get(f"{BASE_URL}/patients")
    assert response.status_code == 200
    assert isinstance(response.json(), list)