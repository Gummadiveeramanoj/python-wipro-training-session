from selenium import webdriver
from selenium.webdriver.common.by import By
class loginpage_PageFactory:

    def __init__(self,driver):
        self.driver=driver;
    @property
    def username(self):
        return self.driver.find_element(By.NAME,"username")

    @property
    def password(self):
        return self.driver.find_element(By.NAME, "password")

    @property
    def loginbutton(self):
        return self.driver.find_element(By.XPATH,"//button[@type='submit']")
   # username=(By.NAME,"username")
   # password=(By.NAME,"password")
   # loginbutton=(By.XPATH,"//button[@type='submit']")

    def enterusername(self,user):
        self.username.send_keys(user)

    def enterpassword(self,pwd):
        self.password.send_keys(pwd)

    def clicklogin(self):
        self.loginbutton.click()