from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Инициализируем драйвер
driver = webdriver.Chrome()

url = (
    "https://bonigarcia.dev/" +
    "selenium-webdriver-java/loading-images.html"
)

# Ждём, пока все три изображения полностью загрузятся
WebDriverWait(driver, 10).until(
    lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3
)

# Получаем список всех изображений
all_images = driver.find_elements(By.TAG_NAME, "img")

# Выбираем третью картинку (индексация с нуля, поэтому третья — это index=2)
third_image = all_images[2]

# Берём атрибут src у третьей картинки
image_src = third_image.get_attribute("src")

# Выводим значение атрибута src в консоль
print(image_src)

# Закрываем браузер
print("Скрипт выполнен успешно!")
driver.quit()
