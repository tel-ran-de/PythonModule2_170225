# Напишите функцию, которая принимает строку с датой и строку с форматом.
# Функция должна вернуть True, если date_string соответствует format_string,
# и False в противном случае.
# Обработку исключений использовать обязательно.

from datetime import datetime

def is_valid_date_format(date_string: str, format_string: str):
    try:
        datetime.strptime(date_string, format_string)
        return True
    except ValueError:
        return False


# Пустые строки:
assert is_valid_date_format("", "%Y-%m-%d") == False
assert is_valid_date_format("   ", "%Y-%m-%d") == False

# Строка с текстом вместо даты:
assert is_valid_date_format("дата: 2025-05-10", "%Y-%m-%d") == False
assert is_valid_date_format("10 мая 2025", "%d-%m-%Y") == False

# Нестандартные символы:
assert is_valid_date_format("2025/05/10", "%Y-%m-%d") == False  # не тот разделитель
assert is_valid_date_format("2025-05-10!", "%Y-%m-%d") == False  # лишний символ

# Числа вне диапазона:
assert is_valid_date_format("2025-00-10", "%Y-%m-%d") == False  # месяц 0
assert is_valid_date_format("2025-12-00", "%Y-%m-%d") == False  # день 0
assert is_valid_date_format("2025-02-29", "%Y-%m-%d") == False  # 2025 не високосный

# Пример использования
date_str1 = "2025-05-10"
format_str1 = "%Y-%m-%d"
date_str2 = "10/05/2025"
format_str2 = "%Y-%m-%d"

print(f"'{date_str1}' соответствует формату '{format_str1}': {is_valid_date_format(date_str1, format_str1)}")
print(f"'{date_str2}' соответствует формату '{format_str2}': {is_valid_date_format(date_str2, format_str2)}")
