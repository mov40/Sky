# shop_autotest/conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="module")
def driver():
    """Инициализация веб-драйвера"""
    firefox_options = Options()
    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()
