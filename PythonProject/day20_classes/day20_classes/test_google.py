import pytest
from day20.driverfactory import getdriver



@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_google_title(browser):
    driver = getdriver(browser)
    driver.get("https://www.google.com/")
    assert "Google" in driver.title
    driver.quit()


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_google_search(browser):
    driver = getdriver(browser)
    driver.get("https://www.google.com/")

    search_box = driver.find_element("name", "q")
    search_box.send_keys("Selenium Grid")
    search_box.submit()

    assert "Selenium Grid" in driver.title
    driver.quit()
