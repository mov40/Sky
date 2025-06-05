import pytest
from selenium import webdriver
from shop_autotest.page_objects.auth_page import AuthPage
from shop_autotest.page_objects.cart_page import CartPage
from shop_autotest.page_objects.checkout_page import CheckoutPage
from shop_autotest.page_objects.main_page import MainPage
import allure  # Импортируем модуль Allure


@pytest.fixture(scope="module")
def driver():
    """
    Инициализация драйвера браузера Firefox.
    """
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


class TestShopPurchase:
    @allure.title("Процесс покупки товара на сайте магазина")
    @allure.description(""" Полный цикл покупок на сайте,
     начиная с авторизации и заканчивая оформлением заказа.""")
    @allure.feature("Покупка товаров онлайн")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_purchase_flow(self, driver):
        """
        Тестирует полный цикл покупки товара на сайте.
        Включает в себя:
        - авторизацию,
        - добавление товаров в корзину,
        - заполнение данных доставки,
        - проверку итоговой суммы.
        """

        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step("Открытие главной страницы сайта"):
            auth_page.open_url("https:адрес/")

        with allure.step("Авторизация пользователя"):
            auth_page.enter_username("ввод логин")
            auth_page.enter_password("ввод пароля")
            auth_page.submit_login()

        with allure.step("Добавление товаров в корзину"):
            main_page.add_backpack_to_cart()
            main_page.add_tshirt_to_cart()
            main_page.add_onesie_to_cart()

        with allure.step("Переход в корзину"):
            main_page.go_to_cart()

        with allure.step("Оформление заказа"):
            cart_page.proceed_to_checkout()

        with allure.step("Заполнение формы доставки"):
            checkout_page.fill_first_name("Иван")
            checkout_page.fill_last_name("Петров")
            checkout_page.fill_postal_code("12345")
            checkout_page.continue_to_summary()

        with allure.step("Чтение итоговой суммы"):
            total = checkout_page.get_total_amount()
            print(f"Итоговая сумма: {total}")

        with allure.step("Проверка итоговой суммы ($58.29)"):
            assert total == "Total: $58.29", "Суммы не совпадают!"
