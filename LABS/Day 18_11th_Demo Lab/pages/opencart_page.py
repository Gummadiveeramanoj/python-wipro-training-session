from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class OpenCartPage:

    def __init__(self, driver):
        self.driver = driver

    # ----------- LOCATORS (PageFactory style) -----------

    @property
    def desktop(self):
        return self.driver.find_element(By.LINK_TEXT, "Desktops")

    @property
    def mac(self):
        return self.driver.find_element(By.LINK_TEXT, "Mac (1)")

    @property
    def mac_heading(self):
        return self.driver.find_element(By.XPATH, "//h2[text()='Mac']")

    @property
    def sort_by(self):
        return self.driver.find_element(By.ID, "input-sort")

    @property
    def addcart(self):
        return self.driver.find_element(
            By.XPATH, "//button[contains(@onclick,'cart.add')]"
        )

    @property
    def search_box(self):
        return self.driver.find_element(By.NAME, "search")

    @property
    def search_btn(self):
        return self.driver.find_element(
            By.XPATH, "//button[@type='button' and contains(@class,'btn-default')]"
        )

    @property
    def search_criteria_box(self):
        return self.driver.find_element(By.ID, "input-search")

    @property
    def description_checkbox(self):
        return self.driver.find_element(By.ID, "description")

    @property
    def criteria_search_btn(self):
        return self.driver.find_element(By.ID, "button-search")

    # ----------- METHODS / ACTIONS -----------

    def click_desktop(self):
        self.desktop.click()

    def click_mac(self):
        self.mac.click()

    def verify_mac_heading(self):
        return self.mac_heading.text

    def select_sort_name_az(self):
        select = Select(self.sort_by)
        select.select_by_visible_text("Name (A - Z)")

    def click_addcart(self):
        self.addcart.click()

    def enter_search_text(self, text):
        self.search_box.clear()
        self.search_box.send_keys(text)

    def click_search_button(self):
        self.search_btn.click()

    def clear_search_criteria(self):
        self.search_criteria_box.clear()

    def click_description_checkbox(self):
        self.description_checkbox.click()

    def click_search_criteria_button(self):
        self.criteria_search_btn.click()
