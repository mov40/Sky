import pytest
from selenium import webdriver
from slow_calculator import SlowCalculatorPage
import allure  # импортируем модуль Allure


@pytest.fixture(scope="module")
def driver():
    """
    Инициализация веб-драйвера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestCalculator:
    @allure.title("Тест расчета суммы на калькуляторе")
    @allure.description(
        "Проверяет простейшую операцию сложения\n"
        " на калькуляторе."
    )
    @allure.feature("Функциональность калькулятора")
    @allure.severity(allure.severity_level.NORMAL)
    def test_calculate_result(self, driver):
        """
        Проверяет правильную работу калькулятора при выполнении сложения.
        """
        calculator_page = SlowCalculatorPage(driver)

        with allure.step("Переход на страницу калькулятора"):
            driver.get(
                "https://bonigarcia.dev/"
                "selenium-webdriver-java/slow-calculator.html"
            )

        with allure.step("Задание задержки вычислений в 45 секунд"):
            calculator_page.set_delay(45)

        with allure.step("Нажатие нужных кнопок калькулятора"):
            calculator_page.click_button(
                SlowCalculatorPage.BUTTON_7_LOCATOR
            )
            calculator_page.click_button(
                SlowCalculatorPage
            )
            calculator_page.click_button(
                SlowCalculatorPage.BUTTON_8_LOCATOR
            )
            calculator_page.click_button(
                SlowCalculatorPage.EQUALS_BUTTON_LOCATOR
            )

        with allure.step("Ожидание результата вычисления"):
            calculator_page.wait_for_result("15")

        with allure.step("Получение итогового результата"):
            final_result = calculator_page.get_result()

        with allure.step("Проверка правильности результата"):
            assert final_result == "15", f"Ошибка: ожидалось '15',\nполучено '{final_result}'"
