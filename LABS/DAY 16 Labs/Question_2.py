from selenium import webdriver
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# 1. Open login page
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
print("Title after opening Login page:", driver.title)
time.sleep(2)

# 2. Navigate to another page on same site (Home page)
driver.get("https://tutorialsninja.com/demo/")
print("Title after navigating to Home page:", driver.title)
time.sleep(2)

# 3. Back navigation
driver.back()
print("Title after back():", driver.title)
time.sleep(2)

# Forward navigation
driver.forward()
print("Title after forward():", driver.title)
time.sleep(2)

# Refresh page
driver.refresh()
print("Title after refresh():", driver.title)
time.sleep(2)

# 5. Close browser
driver.quit()
