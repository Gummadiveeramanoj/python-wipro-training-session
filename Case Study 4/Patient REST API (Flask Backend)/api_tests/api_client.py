import requests

BASE_URL = "http://127.0.0.1:5000/api/patients"

def get_patients():
    return requests.get(BASE_URL)

def add_patient(payload):
    return requests.post(BASE_URL, json=payload)
