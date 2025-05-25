from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем драйвер
driver = webdriver.Firefox()

# Переходим на страницу
driver.get("http://the-internet.herokuapp.com/login")

# Находим поле ввода имени пользователя и вводим "tomsmith"
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("tomsmith")

# Находим поле пароля и вводим "SuperSecretPassword"
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("SuperSecretPassword!")

# Находим кнопку "Login" и нажимаем её
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Ждём появления зелёной плашки с сообщением об успехе
message_element = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "flash.success"))
)

# Получаем текст сообщения и выводим его в консоль
print(f"Текст с зелёной плашки: {message_element.text.strip()}")


# Закрываем браузер
print("Скрипт выполнен успешно!")
driver.quit()
