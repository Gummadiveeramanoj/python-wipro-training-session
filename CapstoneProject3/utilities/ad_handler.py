from selenium.webdriver.common.by import By

def close_ads_and_popups(driver):
    try:
        driver.execute_script("""
            let elements = document.querySelectorAll('[class*="overlay"], [class*="modal"], iframe');
            elements.forEach(el => el.remove());
        """)
    except:
        pass
