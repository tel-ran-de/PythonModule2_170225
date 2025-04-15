from datetime import date

# Получение текущей даты
today = date.today()
print(f"Сегодняшняя дата: {today}")

# Создание заданной даты
specific_date = date(2023, 11, 5)
print(f"Заданная дата: {specific_date}")

# Атрибуты даты
print(f"Год: {specific_date.year}, "
      f"Месяц: {specific_date.month}, "
      f"День: {specific_date.day}")

# День недели (понедельник - 0, воскресенье - 6)
print(f"День недели (weekday): {specific_date.weekday()}")

# День недели (понедельник - 1, воскресенье - 7)
print(f"День недели (isoweekday): {specific_date.isoweekday()}")

# Форматирование в ISO-формате
print(f"ISO-формат даты: {specific_date.isoformat()}")