def test_register_restaurant(client):
    res = client.post("/api/v1/restaurants", json={
        "name": "Food Hub",
        "category": "Veg",
        "location": "Hyderabad"
    })
    assert res.status_code == 201


def test_register_user(client):
    res = client.post("/api/v1/users/register", json={
        "name": "Karthik",
        "email": "karthik@test.com",
        "password": "1234"
    })
    assert res.status_code == 201


def test_place_order(client):
    res = client.post("/api/v1/orders", json={
        "user_id": 1,
        "restaurant_id": 1
    })
    assert res.status_code == 201
