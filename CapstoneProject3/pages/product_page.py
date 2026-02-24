from selenium.webdriver.common.by import By
from CapstoneProject3.pages.base_page import BasePage


class ProductPage(BasePage):

    PRODUCTS_MENU = (By.XPATH, "//a[contains(@href,'/products')]")
    SEARCH_BOX = (By.ID, "search_product")
    SEARCH_BTN = (By.ID, "submit_search")
    ADD_TO_CART = (By.XPATH, "(//a[contains(text(),'Add to cart')])[1]")
    VIEW_CART = (By.XPATH, "//u[contains(text(),'View Cart')]")
    CONTINUE_SHOPPING = (By.XPATH, "//button[contains(text(),'Continue Shopping')]")

    def search_product(self, product):
        self.click(self.PRODUCTS_MENU)
        self.type(self.SEARCH_BOX, product)
        self.click(self.SEARCH_BTN)

    def add_first_product(self):
        # First add to cart
        self.click(self.ADD_TO_CART)
        # Click Continue Shopping — goes back to products page
        self.click(self.CONTINUE_SHOPPING)
        # Add same product again
        self.click(self.ADD_TO_CART)
        # Now go to View Cart
        self.click(self.VIEW_CART)