import requests
import pytest

# Базовый URL сервиса (укажите ваш собственный URL)
Base_URL = "https://ru.yougile.com/api-v2/projects"


# Личный API ключ (если требуется аутентификация)
api_key = ""  # Замените на ваш реальный API ключ


# Заголовки авторизации и тип данных (фиксация единожды и использование везде)
@pytest.fixture
def headers():
    if api_key:
        return {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }


# Фикстура для создания проекта перед каждым тестом
@pytest.fixture
def create_project(headers):  # Передача аргумента headers
    data = {
        "title": "Тестовый проект",  # Название проекта
        "users": []
    }
    response = requests.post(
        Base_URL + "/projects",
        headers=headers,
        json=data
    )
    assert response.status_code == 201, "Ошибка при создании проекта"
    return response.json()["id"]


# Тест №1: успешное создание проекта
def test_create_project_positive(headers):
    data = {
        "title": "Новый тестовый проект",
        "users": []
    }
    response = requests.post(
        Base_URL + "/projects",
        headers=headers,
        json=data
    )
    assert response.status_code == 201, "Проект не был создан"


# Тест №2: ошибка при попытке создать проект с недопустимыми данными
def test_create_project_negative(headers):
    data = {
        "title": "",
        "users": []
    }
    response = requests.post(
        Base_URL + "/projects",
        headers=headers,
        json=data
    )
    assert (
        response.status_code == 400
    ), "Проект с пустым названием был создан (должна быть ошибка)"


# Тест №3: успешное обновление проекта
def test_update_project_positive(create_project, headers):
    project_id = create_project
    data = {"title": "Обновленное название проекта"}
    response = requests.put(
        f"{Base_URL}/projects/{project_id}",
        headers=headers,
        json=data
    )
    assert response.status_code == 200, "Проект не был обновлен"


# Тест №4: ошибка при попытке обновить несуществующий проект
def test_update_project_negative(headers):
    project_id = "не существующий id"
    data = {"title": "Обновленное название проекта"}
    response = requests.put(
        f"{Base_URL}/projects/{project_id}",
        headers=headers,
        json=data
    )
    assert (
        response.status_code == 404
        ), "Несуществующий проект был якобы обновлён"


# Тест №5: успешная загрузка проекта по ID
def test_get_project_positive(create_project, headers):
    project_id = create_project
    response = requests.get(
        f"{Base_URL}/projects/{project_id}",
        headers=headers
    )
    assert response.status_code == 200, "Проект не найден"


# Тест №6: ошибка при попытке получить несуществующий проект
def test_get_project_negative(headers):
    project_id = "не существующий ID"
    response = requests.get(
        f"{Base_URL}/projects/{project_id}",
        headers=headers
    )
    assert (
         response.status_code == 404
         ), "Получился доступ к несуществующему проекту"
