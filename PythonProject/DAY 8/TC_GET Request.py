import requests
get_url1="https://api.restful-api.dev/objects"
response = requests.get(get_url1)
print("get1")
print(response.status_code)
print(response.json())


get_url2="https://api.restful-api.dev/objects?id=3&id=5&id=10"
response_get2 = requests.get(get_url2)
print("get2")
print(response.status_code)
print(response.json())


get_url3="https://api.restful-api.dev/objects/7"
response_get3 = requests.get(get_url3)
print("get3")
print(response.status_code)
print(response.json())


post_url = "https://api.restful-api.dev/objects"
body1={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}
r1=requests.post(post_url,json=body1);
print("post")
print(r1.status_code)
print(r1.json())

put_url="https://api.restful-api.dev/objects/ff8081819782e69e019be40ec1b62ec8"
body2={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}
r2=requests.put(put_url,json=body2);
print("put")
print(r2.status_code)
print(r2.json())

patch_url="https://api.restful-api.dev/objects/ff8081819782e69e019be40ec1b62ec8"
body3={
   "name": "Apple MacBook Pro 16 (Updated Name)"
}
r3=requests.patch(patch_url,json=body3);
print("patch")
print(r3.status_code)
print(r3.json())

delete_url="https://api.restful-api.dev/objects/ff8081819782e69e019be40ec1b62ec8"
r4=requests.delete(delete_url)
print("delete")
print(r4.status_code)
print(r4.json())