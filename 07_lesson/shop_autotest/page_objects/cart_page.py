# shop_autotest/page_objects/cart_page.py

from shop_autotest.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def proceed_to_checkout(self):
        button = self.find_element(self.CHECKOUT_BUTTON)
        button.click()
