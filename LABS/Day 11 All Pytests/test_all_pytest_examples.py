import pytest
import sys

# -------------------------------
# 1️⃣ Assert Statements
# -------------------------------

def test_addition():
    assert 2 + 3 == 5


def test_subtraction():
    assert 5 - 3 == 1, "Subtraction result is incorrect"


# -------------------------------
# 2️⃣ Exception Handling
# -------------------------------

def divide(a, b):
    return a / b


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


# -------------------------------
# 3️⃣ Custom Markers
# -------------------------------

@pytest.mark.smoke
def test_smoke_example():
    assert True


@pytest.mark.regression
def test_regression_example():
    assert True


# -------------------------------
# 4️⃣ Skips and XFail
# -------------------------------

@pytest.mark.skip(reason="Feature not implemented yet")
def test_payment():
    assert True


@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_linux_only():
    assert True


@pytest.mark.xfail(reason="Known bug")
def test_known_issue():
    assert 2 * 2 == 5


# -------------------------------
# 5️⃣ Unit Test Example
# -------------------------------

def multiply(a, b):
    return a * b


def test_multiply():
    assert multiply(3, 4) == 12


# -------------------------------
# 6️⃣ Functional Test Example
# -------------------------------

def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login Successful"
    return "Invalid Credentials"


def test_valid_login():
    assert login("admin", "admin123") == "Login Successful"


def test_invalid_login():
    assert login("user", "wrong") == "Invalid Credentials"
