import pytest

# -----------------------------
# Application Logic (Simulation)
# -----------------------------

def login(username, password):
    if username == "admin" and password == "admin123":
        return {"status": 200, "message": "Login Successful"}
    return {"status": 401, "message": "Login Failed"}


def checkout(cart_amount):
    if cart_amount >= 1000:
        return cart_amount * 0.9   # 10% discount
    return cart_amount


# -----------------------------
# Functional Tests (End-to-End)
# -----------------------------

def test_login_success():
    response = login("admin", "admin123")
    assert response["status"] == 200
    assert response["message"] == "Login Successful"


def test_login_failure():
    response = login("user", "wrongpass")
    assert response["status"] == 401


def test_checkout_with_discount():
    final_amount = checkout(1500)
    assert final_amount == 1350


def test_checkout_without_discount():
    final_amount = checkout(500)
    assert final_amount == 500


# -----------------------------
# Parametrized Functional Test
# -----------------------------

@pytest.mark.parametrize(
    "amount, expected",
    [
        (500, 500),
        (1000, 900),
        (2000, 1800)
    ]
)
def test_checkout_scenarios(amount, expected):
    assert checkout(amount) == expected
