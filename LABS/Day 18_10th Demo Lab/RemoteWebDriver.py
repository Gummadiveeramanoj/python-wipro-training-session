from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

# Create screenshots folder
os.makedirs("Screenshots", exist_ok=True)

# Chrome Options
options = Options()
options.add_argument("--start-maximized")

# Remote WebDriver (Selenium Grid)
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options
)

driver.get("https://tutorialsninja.com/demo/")
driver.save_screenshot("Screenshots/homepage.png")

print("Title:", driver.title)

driver.find_element("xpath", "//span[text()='My Account']").click()
driver.save_screenshot("Screenshots/myaccount.png")

time.sleep(2)
driver.quit()
