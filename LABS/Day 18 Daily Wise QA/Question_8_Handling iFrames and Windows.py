from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")

# ----------------------------
# 1. Switch to iframe
# ----------------------------
driver.switch_to.frame("singleframe")
driver.find_element(By.XPATH, "//input").send_keys("Hello iFrame")

time.sleep(2)

# ----------------------------
# 2. Switch back to main page
# ----------------------------
driver.switch_to.default_content()

# ----------------------------
# 3. Open new window
# ----------------------------
driver.execute_script("window.open('https://google.com');")

# ----------------------------
# 4. Switch between windows
# ----------------------------
windows = driver.window_handles

for window in windows:
    driver.switch_to.window(window)
    print("Window Title:", driver.title)
    time.sleep(1)

# ----------------------------
# 5. Close child window and return to parent
# ----------------------------
driver.switch_to.window(windows[1])
driver.close()

driver.switch_to.window(windows[0])
print("Returned to Parent Window:", driver.title)

driver.quit()
