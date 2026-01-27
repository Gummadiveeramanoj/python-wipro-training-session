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
# xUnit Style Setup & Teardown
# =========================

def setup_module(module):
    print("\n--- setup_module: Runs once before all tests ---")


def teardown_module(module):
    print("\n--- teardown_module: Runs once after all tests ---")


def setup_function(function):
    print("\n>>> setup_function: Runs before each test")


def teardown_function(function):
    print("\n<<< teardown_function: Runs after each test")


# =========================
# Fixtures
# =========================

@pytest.fixture(scope="function")
def numbers():
    print("\n[Fixture] numbers setup (function scope)")
    return 10, 5


@pytest.fixture(scope="module")
def calculator_resource():
    print("\n[Fixture] calculator_resource setup (module scope)")
    yield "Calculator Ready"
    print("\n[Fixture] calculator_resource teardown (module scope)")


# =========================
# Test Cases Using Fixtures
# =========================

def test_addition(numbers, calculator_resource):
    a, b = numbers
    assert add(a, b) == 15


def test_subtraction(numbers):
    a, b = numbers
    assert subtract(a, b) == 5


def test_multiplication(numbers):
    a, b = numbers
    assert multiply(a, b) == 50


def test_division(numbers):
    a, b = numbers
    assert divide(a, b) == 2


def test_division_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
