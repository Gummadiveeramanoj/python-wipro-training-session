from selenium import webdriver
from day18.loginpage import loginpage

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

loginobj = loginpage(driver)
loginobj.enterusername("Admin")
loginobj.enterpassword("admin123")
loginobj.clicklogin()
