import pytest
import requests

@pytest.mark.parametrize("patient", [
    {"name": "Ravi", "age": 30, "gender": "Male"},
    {"name": "Anita", "age": 25, "gender": "Female"}
])
def test_add_patient(base_url, patient):
    r = requests.post(base_url, json=patient)
    assert r.status_code == 201
    assert r.json()["name"] == patient["name"]


def test_get_patients(base_url):
    r = requests.get(base_url)
    assert r.status_code == 200
    assert isinstance(r.json(), list)


@pytest.mark.xfail
def test_invalid_patient(base_url):
    r = requests.post(base_url, json={})
    assert r.status_code == 201


@pytest.mark.skip(reason="Feature not ready")
def test_update_patient():
    pass
