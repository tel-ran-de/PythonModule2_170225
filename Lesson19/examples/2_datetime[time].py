from datetime import time

# Создание заданного времени
specific_time = time(10, 30, 45)
print(f"Заданное время: {specific_time}")

# Создание времени с микросекундами
time_with_microseconds = time(15, 0, 0, 500000)
print(f"Время с микросекундами: {time_with_microseconds}")

# Атрибуты времени
print(f"Час: {specific_time.hour}, Минута: {specific_time.minute}, Секунда: {specific_time.second}, Микросекунда: {specific_time.microsecond}")

# Форматирование в ISO-формате
print(f"ISO-формат времени: {specific_time.isoformat()}")