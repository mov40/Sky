from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем драйвер
driver = webdriver.Chrome()

# Переходим на страницу
driver.get("http://uitestingplayground.com/classattr")

# Ждём, пока кнопка станет кликабельной
print("Начало поиска кнопки...")
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH,
        (
            "//button[contains("
            "concat(' ', normalize-space(@class), ' '), "
            "' btn-primary ') "
            "]"
        )
    ))
)

# Кликаем на кнопку
print("Кнопка найдена, выполняем клик...")
button.click()

# Закрываем браузер
print("Скрипт выполнен успешно!")
driver.quit()
