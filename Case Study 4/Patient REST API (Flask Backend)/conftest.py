import pytest
import requests

@pytest.fixture
def base_url():
    return "http://127.0.0.1:5000/api/patients"
