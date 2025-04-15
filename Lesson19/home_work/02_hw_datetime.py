# Напишите функцию, которая принимает строку с датой и строку с форматом.
# Функция должна вернуть True, если date_string соответствует format_string,
# и False в противном случае.
# Обработку исключений использовать обязательно.

from datetime import datetime

def is_valid_date_format(date_string: str, format_string: str):
    # Допишите код здесь
    return False

# Пример использования
date_str1 = "2025-05-10"
format_str1 = "%Y-%m-%d"
date_str2 = "10/05/2025"
format_str2 = "%Y-%m-%d"

print(f"'{date_str1}' соответствует формату '{format_str1}': {is_valid_date_format(date_str1, format_str1)}")
print(f"'{date_str2}' соответствует формату '{format_str2}': {is_valid_date_format(date_str2, format_str2)}")