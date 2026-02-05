from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open alerts page
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# 1. Trigger JavaScript alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

# Switch to alert
alert = driver.switch_to.alert

# 2. Accept alert and print message
print("Alert Message:", alert.text)
alert.accept()

time.sleep(1)

# 3. Dismiss confirmation pop-up
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
confirm_alert = driver.switch_to.alert
print("Confirm Alert Message:", confirm_alert.text)
confirm_alert.dismiss()

time.sleep(1)

# 4. Enter text in prompt alert and accept it
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
prompt_alert = driver.switch_to.alert
prompt_alert.send_keys("Selenium Test")
prompt_alert.accept()

# 5. Verify result displayed on the page
result = driver.find_element(By.ID, "result").text
print("Result Text:", result)

assert "Selenium Test" in result

# Close browser
time.sleep(2)
driver.quit()
