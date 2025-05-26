from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем драйвер
driver = webdriver.Chrome()

# Переходим на страницу
driver.get("http://uitestingplayground.com/textinput")

# Вводим текст в поле ввода
input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

# Кликаем на синюю кнопку
update_button = driver.find_element(By.ID, "updatingButton")
update_button.click()

# Ждём, пока текст на кнопке изменится на "SkyPro"
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)

# Получаем текст кнопки и выводим в консоль
final_button = driver.find_element(By.ID, "updatingButton")
final_button_text = final_button.text
print(final_button_text)

# Закрываем браузер
print("Скрипт выполнен успешно!")
driver.quit()
