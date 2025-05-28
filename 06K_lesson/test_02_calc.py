import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="module")
def driver():
    """Инициализация веб-драйвера"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestCalculator:

    def test_calculate_result(self, driver):
        # Открываем нужную страницу
        driver.get('https://bonigarcia.dev/selenium-webdriver-java/'
                   'slow-calculator.html')

        # Задать задержку расчета
        delay_input = driver.find_element(By.ID, 'delay')
        delay_input.clear()
        delay_input.send_keys('45')

        # Нажимаем на кнопки калькулятора
        button_7 = driver.find_element(By.XPATH, '//span[.="7"]')
        button_plus = driver.find_element(
            By.XPATH, '//span[@class="operator btn btn-outline-success"]'
        )
        button_8 = driver.find_element(By.XPATH, '//span[.="8"]')
        button_equals = driver.find_element(
            By.XPATH, '//span[@class="btn btn-outline-warning"]'
        )

        button_7.click()
        button_plus.click()
        button_8.click()
        button_equals.click()

        # Ждём появления результата с ожиданием текста
        wait = WebDriverWait(driver, 60)  # увеличили таймаут до 60 секунд
        result_field = wait.until(
            lambda drv: drv.find_element(
                By.CLASS_NAME, 'screen'
            ).text.strip() == '15',
            message="Результат не равен 15!"
        )

        # Проверяем результат
        assert result_field, "Результат не равен 15"
