import pytest

# =========================
# Calculator Module
# =========================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


# =========================
# Pytest Test Cases
# =========================

def test_addition():
    assert add(2, 3) == 5


def test_subtraction():
    assert subtract(10, 4) == 6


def test_multiplication():
    assert multiply(3, 5) == 15


def test_division():
    assert divide(20, 4) == 5


def test_division_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

