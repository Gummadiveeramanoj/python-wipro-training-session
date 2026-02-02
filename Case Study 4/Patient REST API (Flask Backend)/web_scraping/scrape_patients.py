import requests
from bs4 import BeautifulSoup

# API / Web URL
URL = "http://127.0.0.1:5000/api/patients"

response = requests.get(URL)
patients = response.json()

print("Patient Details")
print("-" * 30)

for patient in patients:
    print(f"Name   : {patient.get('name')}")
    print(f"Age    : {patient.get('age')}")
    print(f"Disease: {patient.get('disease')}")
    print(f"Doctor : {patient.get('doctor')}")
    print("-" * 30)
