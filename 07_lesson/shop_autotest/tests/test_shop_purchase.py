# shop_autotest/tests/test_shop_purchase.py

import pytest
from selenium import webdriver
from shop_autotest.page_objects.auth_page import AuthPage
from shop_autotest.page_objects.cart_page import CartPage
from shop_autotest.page_objects.checkout_page import CheckoutPage
from shop_autotest.page_objects.main_page import MainPage


@pytest.fixture(scope="module")
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


class TestShopPurchase:

    def test_purchase_flow(self, driver):
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # Открытие сайта
        auth_page.open_url("https://www.saucedemo.com/")

        # Авторизация пользователя
        auth_page.enter_username("standard_user")
        auth_page.enter_password("secret_sauce")
        auth_page.submit_login()

        # Добавление товаров в корзину
        main_page.add_backpack_to_cart()
        main_page.add_tshirt_to_cart()
        main_page.add_onesie_to_cart()

        # Переход в корзину
        main_page.go_to_cart()

        # Оформление заказа
        cart_page.proceed_to_checkout()

        # Заполнение формы доставки
        checkout_page.fill_first_name("Иван")
        checkout_page.fill_last_name("Петров")
        checkout_page.fill_postal_code("12345")
        checkout_page.continue_to_summary()

        # Чтение итоговой суммы
        total = checkout_page.get_total_amount()
        print(f"Итоговая сумма: {total}")

        # Проверка итоговой суммы ($58.29)
        assert total == "Total: $58.29", "Суммы не совпадают!"
