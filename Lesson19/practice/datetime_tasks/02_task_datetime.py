# Создайте объект datetime, представляющий 10 часов 30 минут утра 16 апреля 2025 года, и выведите его на экран.


from datetime import datetime, date, time

specific_date = date(2025, 4, 16)

specific_time = time(10, 30, 45)
print(specific_date)
print(f"Заданное время: {specific_time}")
