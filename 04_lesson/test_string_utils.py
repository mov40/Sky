import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# Тесты для функции capitalize
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("Тест", "Тест"),  # доп. проверка русской строки
    ("123", "123"),  # доп. проверка чисел
    ("04 апреля 2023", "04 апреля 2023"),  # доп. проверка строки с пробелами
])
def test_capitalize_positive(input_str, expected):
    result = string_utils.capitalize(input_str)
    assert result == expected, f"Ошибка капитализации строки '{input_str}'"


@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                     # пустая строка
    (" ", " "),                   # строка с пробелом
    (None, TypeError),            # проверка на None
])
def test_capitalize_negative(input_str, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            string_utils.capitalize(input_str)
    else:
        result = string_utils.capitalize(input_str)
        assert result == expected, (
            f"Ошибка капитализации строки '{input_str}'"
        )


# Тесты для функции trim
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    (" hello world ", "hello world "),     # внутренняя пробельная зона
    (" python ", "python "),
    ("04 апреля 2023", "04 апреля 2023"),  # проверка строки с пробелами
])
def test_trim_positive(input_str, expected):
    result = string_utils.trim(input_str)
    assert result == expected, (
        f"Ошибка обрезки пробелов в строке '{input_str}'"
    )


@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                 # пустая строка
    (" ", " "),               # строка с единственным пробелом
    (None, TypeError),        # проверка на None
])
def test_trim_negative(input_str, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            string_utils.trim(input_str)
    else:
        result = string_utils.trim(input_str)
        assert result == expected, (
            f"Ошибка обрезки пробелов в строке '{input_str}'"
        )


# Тесты для функции contains
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "P", True),
    ("SkyPro", "r", True),
    ("Тест", "т", True),           # русская строка
    ("123", "2", True),            # цифровая строка
    ("04 апреля 2023", "а", True),  # строка с пробелами
])
def test_contains_positive(input_str, symbol, expected):
    result = string_utils.contains(input_str, symbol)
    assert result == expected, f"Ошибка проверки наличия символа '{symbol}'"
    f"в строке '{input_str}'"


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "u", False),
    ("SkyPro", "z", False),
    ("SkyPro", "", False),
    ("", "a", False),             # пустая строка
    (" ", "x", False),            # строка с пробелом
    (None, "a", TypeError),       # проверка на None
])
def test_contains_negative(input_str, symbol, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            string_utils.contains(input_str, symbol)
    else:
        result = string_utils.contains(input_str, symbol)
        assert result == expected, (
            f"Ошибка проверки отсутствия символа '{symbol}'"
            f"в строке '{input_str}'"
        )


# Тесты для функции delete_symbol
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Python", "h", "Pyton"),
    ("Тест", "т", "ес"),          # русская строка
    ("123", "2", "13"),           # цифровая строка
    ("04 апреля 2023", "а", "04 преля 2023"),  # строка с пробелами
])
def test_delete_symbol_positive(input_str, symbol, expected):
    result = string_utils.delete_symbol(input_str, symbol)
    assert result == expected, (
        f"Ошибка удаления символа '{symbol}'"
        f"из строки '{input_str}'"
    )


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "xyz", "SkyPro"),
    ("SkyPro", "SkyPro", ""),
    ("", "a", ""),                # пустая строка
    (" ", "x", " "),              # строка с пробелом
    (None, "a", TypeError),       # проверка на None
])
def test_delete_symbol_negative(input_str, symbol, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            string_utils.delete_symbol(input_str, symbol)
    else:
        result = string_utils.delete_symbol(input_str, symbol)
        assert result == expected, (
            f"Ошибка удаления символа '{symbol}'"
            f"из строки '{input_str}'"
        )
