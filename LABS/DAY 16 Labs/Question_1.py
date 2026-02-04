from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open login page
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
print("Page Title:", driver.title)

# Enter Email using ID locator
driver.find_element(By.ID, "input-email").send_keys("gummadiveeramanoj@gmail.com")

# Enter Password using ID locator
driver.find_element(By.ID, "input-password").send_keys("Manoj@2004")

# Click Login button using XPath
driver.find_element(By.XPATH, "//input[@value='Login']").click()

time.sleep(2)

# Validate successful login message using CSS Selector
heading = driver.find_element(By.CSS_SELECTOR, "#content h2").text

if heading == "My Account":
    print("Login Successful – Test Passed")
else:
    print("Login Failed – Test Failed")

# Close browser
driver.quit()
