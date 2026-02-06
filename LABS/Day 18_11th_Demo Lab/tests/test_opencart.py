from selenium import webdriver
import time
from pages.opencart_page import OpenCartPage

def test_opencart_flow():

    driver = webdriver.Firefox()
    driver.maximize_window()

    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(3)

    obj = OpenCartPage(driver)

    # Step 1: Click Desktops
    obj.click_desktop()
    time.sleep(2)

    # Step 2: Click Mac
    obj.click_mac()
    time.sleep(3)

    # Step 3: Verify Mac Heading
    heading = obj.verify_mac_heading()
    print("Heading is:", heading)

    assert heading == "Mac"

    # Step 4: Sort Name (A-Z)
    obj.select_sort_name_az()
    time.sleep(2)

    # Step 5: Add to Cart
    obj.click_addcart()
    time.sleep(3)
    print("Mac product added to cart successfully!")

    # Step 6: Search Mobile
    obj.enter_search_text("Mobile")
    obj.click_search_button()
    time.sleep(3)

    # Step 7: Search in descriptions
    obj.click_description_checkbox()
    time.sleep(2)

    obj.click_search_criteria_button()
    time.sleep(3)

    # Step 8: Clear search criteria
    obj.clear_search_criteria()
    time.sleep(2)

    # Step 9: Search Monitors
    obj.enter_search_text("Monitors")
    obj.click_search_button()
    time.sleep(3)

    print("Search completed successfully!")

    driver.quit()
