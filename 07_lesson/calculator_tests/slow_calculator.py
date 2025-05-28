from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:

    # Локаторы элементов страницы
    DELAY_INPUT_LOCATOR = (By.ID, 'delay')  # Поле задержки вычислений
    BUTTON_7_LOCATOR = (By.XPATH, '//span[.="7"]')  # Кнопка цифры 7
    PLUS_BUTTON_LOCATOR = (
        By.XPATH,
        '//span[@class="operator btn btn-outline-success"]'  # Кнопка +
    )
    BUTTON_8_LOCATOR = (By.XPATH, '//span[.="8"]')  # Кнопка цифры 8
    EQUALS_BUTTON_LOCATOR = (
        By.XPATH,
        '//span[@class="btn btn-outline-warning"]'  # Кнопка =
    )
    RESULT_FIELD_LOCATOR = (By.CLASS_NAME, 'screen')  # Результат вычисления

    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, seconds: int):
        """
        Устанавливает задержку перед выполнением операции.
        :param seconds: Количество секунд задержки.
        """
        delay_input = self.driver.find_element(*self.DELAY_INPUT_LOCATOR)
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, locator: tuple[str, str]):
        """
        Кликает на заданную кнопку.
        :param locator: Селектор элемента (например, XPATH или ID).
        """
        button = self.driver.find_element(*locator)
        button.click()

    def get_result(self) -> str:
        """
        Возвращает отображаемый результат на экране калькулятора.
        """
        element = self.driver.find_element(*self.RESULT_FIELD_LOCATOR)
        return element.text.strip()

    def wait_for_result(self, expected_value: str, timeout=60):
        """
        Ожидает пока результат станет равным ожидаемому значению.
        :param expected_value: Ожидаемый результат.
        :param timeout: Таймаут ожидания (секунды).
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(
                self.RESULT_FIELD_LOCATOR,
                expected_value
            ),
            f"Результат не стал '{expected_value}'"
        )
