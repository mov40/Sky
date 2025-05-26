import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    """Инициализация веб-драйвера"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestFormSubmission:

    def test_fill_and_submit(self, driver):
        # Открываем нужную страницу
        driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/'
            'data-types.html'
        )

        # Добавляем ожидание загрузки элементов
        wait = WebDriverWait(driver, 30)

        # Заполняем форму
        first_name_field = wait.until(
            EC.presence_of_element_located((By.NAME, 'first-name'))
        )

        last_name_field = wait.until(
            EC.presence_of_element_located((By.NAME, 'last-name'))
        )

        address_field = wait.until(
            EC.presence_of_element_located((By.NAME, 'address'))
        )

        email_field = wait.until(
            EC.presence_of_element_located((By.NAME, 'e-mail'))
        )

        phone_number_field = wait.until(
            EC.presence_of_element_located((By.NAME, 'phone'))
        )

        city_field = wait.until(
            EC.presence_of_element_located((By.NAME, 'city'))
        )

        country_field = wait.until(
            EC.presence_of_element_located((By.NAME, 'country'))
        )

        job_position_field = wait.until(
            EC.presence_of_element_located((By.NAME, 'job-position'))
        )

        company_field = wait.until(
            EC.presence_of_element_located((By.NAME, 'company'))
        )

        # Ожидаем кнопку с верным классом (btn btn-outline-primary)
        submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.btn.btn-outline-primary')
            )
        )

        first_name_field.send_keys('Иван')
        last_name_field.send_keys('Петров')
        address_field.send_keys('Ленина, 55-3')
        email_field.send_keys('test@skypro.com')
        phone_number_field.send_keys('+7985899998787')
        # Оставляем Zip Code пустым
        city_field.send_keys('Москва')
        country_field.send_keys('Россия')
        job_position_field.send_keys('QA')
        company_field.send_keys('SkyPro')

        # Нажимаем кнопку Submit
        submit_button.click()

        # Добавляем ожидание устойчивости страницы после отправки формы
        wait.until(EC.staleness_of(first_name_field))

        # Проверяем цвет поля ZIP Code (должен стать красным)
        error_class_zipcode = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#zip-code.alert-danger')
            )
        )
        assert error_class_zipcode.is_displayed(), \
            "Поле ZIP Code не помечено как ошибочное"

        # Проверяем другие поля (они должны остаться зелёными)
        input_fields_ids = [
            'first-name',
            'last-name',
            'address',
            'city',
            'country',
            'e-mail',
            'phone',
            'job-position',
            'company'
        ]

        for field_id in input_fields_ids:
            success_field = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, f'#{field_id}.alert-success')
                )
            )
            assert success_field.is_displayed(), \
                f"Поле {field_id} не отмечено как успешное"
