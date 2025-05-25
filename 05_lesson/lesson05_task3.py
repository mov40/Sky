from selenium import webdriver
from selenium.webdriver.common.by import By


# Инициализируем драйвер
driver = webdriver.Firefox()

# Переходим на страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Находим поле ввода
input_field = driver.find_element(By.TAG_NAME, "input")

# Отправляем текст "Sky"
input_field.send_keys("Sky")

# Очищаем поле
input_field.clear()

# Отправляем текст "Pro"
input_field.send_keys("Pro")


# Закрываем браузер
print("Скрипт выполнен успешно!")
driver.quit()
