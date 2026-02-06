from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.amazon.in")

time.sleep(5)


driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

time.sleep(5)
driver.quit()
