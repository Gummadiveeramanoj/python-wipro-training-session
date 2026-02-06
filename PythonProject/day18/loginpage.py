from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class loginpage:

    def __init__(self, driver):          # ✅ MUST accept driver
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enterusername(self, username):
        self.wait.until(
            EC.visibility_of_element_located((By.NAME, "username"))
        ).send_keys(username)

    def enterpassword(self, password):
        self.driver.find_element(By.NAME, "password").send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
print("Constructor called")
