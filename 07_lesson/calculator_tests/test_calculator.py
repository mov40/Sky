import pytest
from selenium import webdriver
from slow_calculator import SlowCalculatorPage


@pytest.fixture(scope="module")
def driver():
    """Инициализация веб-драйвера."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestCalculator:

    def test_calculate_result(self, driver):
        calculator_page = SlowCalculatorPage(driver)

        # Переходим на страницу калькулятора
        driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )

        # Установим задержку вычислений в 45 секунд
        calculator_page.set_delay(45)

        # Нажмем нужные кнопки калькулятора
        calculator_page.click_button(SlowCalculatorPage.BUTTON_7_LOCATOR)
        calculator_page.click_button(SlowCalculatorPage.PLUS_BUTTON_LOCATOR)
        calculator_page.click_button(SlowCalculatorPage.BUTTON_8_LOCATOR)
        calculator_page.click_button(SlowCalculatorPage.EQUALS_BUTTON_LOCATOR)

        # Подождем появление правильного результата
        calculator_page.wait_for_result("15")

        # Получим итоговое значение поля результата
        final_result = calculator_page.get_result()

        # Проведем проверку результата
        assert final_result == "15", f"Ожидалось '15', получено {final_result}"
