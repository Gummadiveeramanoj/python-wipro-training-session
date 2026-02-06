import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# ---------------------------------
# CONFIGURATION
# ---------------------------------
URL = "https://tutorialsninja.com/demo/"

# ---------------------------------
# BASE PAGE (Reusable Methods)
# ---------------------------------
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def enter_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def select_dropdown(self, locator, value):
        Select(self.driver.find_element(*locator)).select_by_visible_text(value)

# ---------------------------------
# PAGE OBJECT (Login Page)
# ---------------------------------
class LoginPage(BasePage):

    MY_ACCOUNT = (By.XPATH, "//span[text()='My Account']")
    LOGIN = (By.LINK_TEXT, "Login")
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")

    def login(self, email, password):
        self.click(self.MY_ACCOUNT)
        self.click(self.LOGIN)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

# ---------------------------------
# PYTEST FIXTURE (Browser Setup)
# ---------------------------------
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()

# ---------------------------------
# TEST SCRIPT
# ---------------------------------
def test_login_pom(setup):
    driver = setup
    login_page = LoginPage(driver)

    login_page.login("test@gmail.com", "test123")

    print("Login Test Executed Successfully using POM Framework")
