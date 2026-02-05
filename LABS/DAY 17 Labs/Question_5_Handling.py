from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open web form page
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# 1. Fill text boxes
driver.find_element(By.NAME, "my-text").send_keys("Manu")
driver.find_element(By.NAME, "my-password").send_keys("12345")

# 2. Select radio button
driver.find_element(By.ID, "my-radio-2").click()

# 2. Select checkbox
driver.find_element(By.ID, "my-check-2").click()

# 3. Select option from dropdown using Select class
dropdown = Select(driver.find_element(By.NAME, "my-select"))
dropdown.select_by_visible_text("Two")

# Small wait
time.sleep(2)

# 4. Submit the form
driver.find_element(By.TAG_NAME, "button").click()

# 5. Verify confirmation message
message = driver.find_element(By.ID, "message").text
print("Confirmation Message:", message)

assert "Received!" in message

# Close browser
time.sleep(2)
driver.quit()
