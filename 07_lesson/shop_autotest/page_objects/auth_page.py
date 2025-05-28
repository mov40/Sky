from shop_autotest.base_page import BasePage
from selenium.webdriver.common.by import By


class AuthPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def enter_username(self, username):
        field = self.find_element(self.USERNAME_FIELD)
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.find_element(self.PASSWORD_FIELD)
        field.clear()
        field.send_keys(password)

    def submit_login(self):
        button = self.find_element(self.LOGIN_BUTTON)
        button.click()
