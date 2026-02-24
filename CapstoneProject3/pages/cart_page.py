from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from CapstoneProject3.pages.base_page import BasePage


class CartPage(BasePage):

    CART_TABLE = (By.ID, "cart_info_table")
    REMOVE_BTN = (By.XPATH, "//a[@class='cart_quantity_delete']")

    def remove_product(self):
        self.wait.until(EC.visibility_of_element_located(self.CART_TABLE))
        self.click(self.REMOVE_BTN)