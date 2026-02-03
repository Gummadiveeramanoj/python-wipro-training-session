import requests

BASE_URL = "http://127.0.0.1:5000/api/patients"

def test_add_patient():
    payload = {
        "id": 1,
        "name": "Ravi",
        "age": 30,
        "gender": "Male",
        "contact": "9876543210",
        "disease": "Fever",
        "doctor": "Dr. Rao"
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201

def test_get_patients():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
