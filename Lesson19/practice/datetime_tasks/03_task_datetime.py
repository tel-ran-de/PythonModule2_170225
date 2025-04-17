# "Название сегодняшнего дня недели"

# Напишите функцию, которая возвращает название сегодняшнего дня недели на русском языке
# (например, "понедельник", "вторник" и т.д.) с учетом текущей даты.

from datetime import date
from datetime import datetime, date, time


def get_today_day_name(today: date) -> str:
    """Возвращает название сегодняшнего дня недели на русском языке."""
<<<<<<< HEAD

    # Получение текущей даты и времени
    now = datetime.now()
    print(f"Текущая дата и время: {now}")
    print(f"Только дата: {now.date()}")
    print(now.strftime("%a, %d %b %y"))  # Сокр.ДеньНедели, День Сокр.Месяца Год (Thu, 26 Oct 23)
    

get_today_day_name(date.today())
# Получение текущей даты и времени
=======
    day_names = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
    day_index = today.weekday()
    return day_names[day_index]

our_data = date(2025, 4, 13)
print(get_today_day_name(our_data))
>>>>>>> 313dbff6d8a5cacc923f6a78edd0509c9d16bad3
