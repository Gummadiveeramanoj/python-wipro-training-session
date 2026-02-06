from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in")
time.sleep(2)


driver.execute_script("alert('Hello Amazon')")
time.sleep(1)


alert = driver.switch_to.alert
print("Alert text is:", alert.text)
alert.accept()   # Click OK
time.sleep(1)


driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)

driver.quit()
