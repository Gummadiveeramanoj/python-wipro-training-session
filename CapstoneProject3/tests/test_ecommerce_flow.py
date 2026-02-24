import pytest
import logging
from CapstoneProject3.config.config import BASE_URL
from CapstoneProject3.pages.login_page import LoginPage
from CapstoneProject3.pages.product_page import ProductPage
from CapstoneProject3.pages.cart_page import CartPage
from CapstoneProject3.utilities.data_loader import load_users

logging.basicConfig(level=logging.INFO)

users = load_users()

@pytest.mark.parametrize(
    "user",
    users,
    ids=[user["name"] for user in users]
)
def test_complete_ecommerce_flow(driver, user):

    logging.info(f"Starting test for {user['name']}")

    driver.get(BASE_URL)

    login = LoginPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    logging.info("Logging in")
    login.login(user["email"], user["password"])
    assert "Logged in as" in driver.page_source

    logging.info(f"Searching product: {user['product']}")
    product.search_product(user["product"])
    assert "Searched Products" in driver.page_source

    logging.info("Adding product to cart — first time")
    logging.info("Coming back to products page")
    logging.info("Adding same product to cart — second time")
    product.add_first_product()
    assert "Shopping Cart" in driver.page_source

    logging.info("Removing from cart")
    cart.remove_product()

    logging.info("Logging out")
    login.logout()
    assert "Login to your account" in driver.page_source

    logging.info(f"Test completed for {user['name']}")