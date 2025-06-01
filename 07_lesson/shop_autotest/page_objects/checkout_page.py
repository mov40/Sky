# shop_autotest/page_objects/checkout_page.py

from shop_autotest.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def fill_first_name(self, first_name):
        field = self.find_element(self.FIRST_NAME_FIELD)
        field.clear()
        field.send_keys(first_name)

    def fill_last_name(self, last_name):
        field = self.find_element(self.LAST_NAME_FIELD)
        field.clear()
        field.send_keys(last_name)

    def fill_postal_code(self, postal_code):
        field = self.find_element(self.POSTAL_CODE_FIELD)
        field.clear()
        field.send_keys(postal_code)

    def continue_to_summary(self):
        button = self.find_element(self.CONTINUE_BUTTON)
        button.click()

    def get_total_amount(self):
        label = self.find_element(self.TOTAL_LABEL)
        return label.text
