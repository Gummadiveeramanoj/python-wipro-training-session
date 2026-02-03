import requests

response = requests.get("http://127.0.0.1:5000/api/patients")
patients = response.json()   # JSON deserialization

for p in patients:
    print(p["name"], p["age"], p.get("disease"))
