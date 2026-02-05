from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time

#! Part 1: Launch Application

driver=webdriver.Edge()
driver.maximize_window()
wait=WebDriverWait(driver,15)

driver.get("https://tutorialsninja.com/demo/")

#~ check the title

actual_title=driver.title

if actual_title=="Your Store":
    print("Title Verified")
else:
    print("Title Not Verified")

#~ click myaccount

my_account=wait.until(
    EC.element_to_be_clickable((By.XPATH,"//span[text()='My Account']"))
)
my_account.click()

#~ click register option

register_option=wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT,"Register"))
)
register_option.click()

register_heading=wait.until(
    EC.visibility_of_element_located((By.XPATH, "//h1[text()='Register Account']" ))
).text

if register_heading=="Register Account":
    print("Register heading verified")
else:
    print("Register heading not verified")


