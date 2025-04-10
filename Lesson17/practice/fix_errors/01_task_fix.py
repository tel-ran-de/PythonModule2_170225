# Дана функция
def celsius_to_fahrenheit(celsius: int | float) -> float:
    "Конвертация температуры из Цельсия в Фаренгейт"
    return (celsius * 9 / 5) + 32


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(100) == 212.0

    return test_celsius_to_fahrenheit


test_celsius_to_fahrenheit()
# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
