from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https:\\www.google.com")
title = driver.title
currenturl = driver.current_url
pagesource = driver.page_source
print(title)
print(currenturl)
print(pagesource)
