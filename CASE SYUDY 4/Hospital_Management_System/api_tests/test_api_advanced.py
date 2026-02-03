import requests
import pytest

def test_invalid_patient(base_url):
    response = requests.post(base_url, json={"name": "", "age": -1})
    assert response.status_code == 400

@pytest.mark.parametrize("patient", [
    {"id": 2, "name": "A", "age": 25},
    {"id": 3, "name": "B", "age": 40}
])
def test_multiple_patients(base_url, patient):
    r = requests.post(base_url, json=patient)
    assert r.status_code == 201
