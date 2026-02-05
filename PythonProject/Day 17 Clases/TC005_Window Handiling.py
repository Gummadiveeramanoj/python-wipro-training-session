from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.get("https://letcode.in/window")
time.sleep(5)
driver.find_element(By.ID,"multi").click()
time.sleep(5)
windows=driver.window_handles
for child in windows:
    driver.switch_to.window(child)
    time.sleep(5)
    print("url",driver.current_url)