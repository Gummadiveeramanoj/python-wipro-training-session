from selenium import webdriver
import time

def test_orangehrm_title_url():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)

    print("Page Title:", driver.title)
    print("Current URL:", driver.current_url)

    assert "OrangeHRM" in driver.title

    driver.quit()
