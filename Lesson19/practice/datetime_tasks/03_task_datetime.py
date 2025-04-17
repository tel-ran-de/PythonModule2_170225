# "Название сегодняшнего дня недели"

# Напишите функцию, которая возвращает название сегодняшнего дня недели на русском языке
# (например, "понедельник", "вторник" и т.д.) с учетом текущей даты.

from datetime import date


def get_today_day_name(today: date) -> str:
    """Возвращает название сегодняшнего дня недели на русском языке."""
    day_names = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
    day_index = today.weekday()
    return day_names[day_index]

our_data = date(2025, 4, 13)
print(get_today_day_name(our_data))
