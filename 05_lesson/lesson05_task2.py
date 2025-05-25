from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем драйвер
driver = webdriver.Chrome()

# Переходим на страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Ждём, пока кнопка станет кликабельной
print("Начало поиска кнопки...")
wait = WebDriverWait(driver, 10)  # ожидание до 10 секунд
button = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//button[contains(text(), 'Button with Dynamic ID')]"
    ))
)
# Кликаем на кнопку
print("Кнопка найдена, выполняем клик...")
button.click()

# Закрываем браузер
print("Скрипт выполнен успешно!")
driver.quit()
