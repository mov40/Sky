import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    """Инициализация веб-драйвера"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestShopPurchase:

    def test_purchase_total(self, driver):
        # Открываем главную страницу магазина
        driver.get("https://www.saucedemo.com/")

        # Авторизуемся как user
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        # Добавляем товары в корзину
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        # Переходим в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Нажимаем кнопку "Checkout"
        driver.find_element(By.ID, "checkout").click()

        # Заполняем поля
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        # Читаем итоговую сумму (она появляется мгновенно)
        total_label = driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label"
        )
        total = total_label.text
        print(f"Проверяем итоговую сумму: {total}")
        assert total == "Total: $58.29", \
            "Итоговая сумма отличается от ожидаемой!"
