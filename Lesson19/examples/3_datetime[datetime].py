from datetime import datetime, date, time

# Получение текущей даты и времени
now = datetime.now()
print(f"Текущая дата и время: {now}")

# Создание заданной даты и времени
specific_datetime = datetime(2024, 1, 20, 14, 45, 30)
print(f"Заданная дата и время: {specific_datetime}")

# Комбинирование date и time объектов
today = date.today()
noon = time(12, 0, 0)
today_noon = datetime.combine(today, noon)
print(f"Сегодня в полдень: {today_noon}")

# Получение объектов date и time из datetime
print(f"Только дата: {now.date()}")
print(f"Только время: {now.time()}")