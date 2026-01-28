import pytest
import sys

# -----------------------------
# Application logic
# -----------------------------
def add(a, b):
    return a + b

def divide(a, b):
    return a / b


# -----------------------------
# Parameterized test
# -----------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (-1, 1, 0)
    ]
)
def test_addition(a, b, expected):
    assert add(a, b) == expected


# -----------------------------
# CLI option usage
# -----------------------------
def test_environment_value(env):
    assert env in ["dev", "qa", "prod"]


# -----------------------------
# Skip test
# -----------------------------
@pytest.mark.skip(reason="Feature under development")
def test_skipped_feature():
    assert False


# -----------------------------
# Conditional skip
# -----------------------------
@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_linux_only():
    assert True


# -----------------------------
# Expected failure
# -----------------------------
@pytest.mark.xfail(reason="Known bug: division by zero not handled")
def test_divide_by_zero():
    divide(10, 0)
