from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox()
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()
print("tilte is",driver.title)
driver.get("https://www.google.com/")
print("tilte is",driver.title)
time.sleep(5)
driver.back()
print("title after back",driver.title)
driver.forward()
print("title after forward",driver.title)
