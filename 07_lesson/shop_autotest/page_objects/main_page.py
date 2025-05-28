# shop_autotest/page_objects/main_page.py

from shop_autotest.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TO_CART_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_TO_CART_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        button = self.find_element(self.ADD_TO_CART_BACKPACK)
        button.click()

    def add_tshirt_to_cart(self):
        button = self.find_element(self.ADD_TO_CART_TSHIRT)
        button.click()

    def add_onesie_to_cart(self):
        button = self.find_element(self.ADD_TO_CART_ONESIE)
        button.click()

    def go_to_cart(self):
        link = self.find_element(self.SHOPPING_CART_LINK)
        link.click()
