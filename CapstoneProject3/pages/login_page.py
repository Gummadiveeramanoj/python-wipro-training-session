from selenium.webdriver.common.by import By
from  CapstoneProject3.pages.base_page import BasePage

class LoginPage(BasePage):

    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    EMAIL = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BTN = (By.XPATH, "//button[@data-qa='login-button']")
    LOGGED_IN = (By.XPATH, "//a[contains(text(),'Logged in as')]")
    LOGOUT = (By.XPATH, "//a[contains(text(),'Logout')]")

    def login(self, email, password):
        self.click(self.LOGIN_LINK)
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def logout(self):
        self.click(self.LOGOUT)
