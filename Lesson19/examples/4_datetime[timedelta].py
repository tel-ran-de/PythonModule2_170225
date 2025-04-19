from datetime import timedelta, date, datetime

# Создание timedelta объектов
delta1 = timedelta(days=7)
delta2 = timedelta(hours=3, minutes=30)
delta3 = timedelta(weeks=2, days=1, seconds=10)
print(f"Дельта 1: {delta1}")
print(f"Дельта 2: {delta2}")
print(f"Дельта 3: {delta3}")

# Арифметика с датами
today = date.today()
one_week_later = today + delta1
yesterday = today - timedelta(days=1)
print(f"Через неделю: {one_week_later}")
print(f"Вчера: {yesterday}")

# Арифметика с datetime
now = datetime.now()
in_two_hours = now + timedelta(hours=2)
five_minutes_ago = now - timedelta(minutes=5)
print(f"Через два часа: {in_two_hours}")
print(f"Пять минут назад: {five_minutes_ago}")

# Разница между двумя датами (результат - timedelta)
date1 = date(2023, 10, 15)
date2 = date(2023, 10, 20)
difference = date2 - date1
print(f"Разница между датами: {difference}")
print(f"Количество дней в разнице: {difference.days}")