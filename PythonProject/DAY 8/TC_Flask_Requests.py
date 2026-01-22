import requests
import json
# -----------get----------------#
get_url="http://127.0.0.1:5000/users"

response=requests.get(get_url)
print(response.status_code)
# print(response.text)
data=json.loads(response.text)
print(data)

post_url = "http://127.0.0.1:5000/users"
body = {
   "name": "varsha gowtham"

}

r2 = requests.post(post_url, json=body)
print(r2.status_code)
data = json.loads(response.text)
print(r2.json())

put_url = "http://127.0.0.1:5000/users/1"
body = {
   "name": "varsha gowtham"

}

r3 = requests.put(put_url, json=body)
print(r3.status_code)
data = json.loads(response.text)
print(r3.json())

patch_url = "http://127.0.0.1:5000/users/2"
body = {
   "name": "varsha gowtham"

}

r4 = requests.patch(patch_url, json=body)
print(r4.status_code)
data = json.loads(response.text)
print(r4.json())

delete_url = "http://127.0.0.1:5000/users/1"
r5 = requests.delete(delete_url)

