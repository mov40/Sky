from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем драйвер
driver = webdriver.Chrome()

# Переходим на страницу
driver.get("http://uitestingplayground.com/ajax")

# Нажимаем на кнопку
ajax_button = driver.find_element(By.ID, "ajaxButton")
ajax_button.click()

# Ждём появления текста в зелёной плашке (только явное ожидание)
message = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
)

# Выводим полученный текст
print(message.text.strip())

# Закрываем браузер
print("Скрипт выполнен успешно!")
driver.quit()
