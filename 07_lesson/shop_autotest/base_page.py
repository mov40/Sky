# shop_autotest/page_objects/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, by_locator):
        return self.driver.find_element(*by_locator)

    def wait_until_visible(self, by_locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.visibility_of_element_located(by_locator))
        return element
