# "Получение завтрашней даты"
#
# Напишите функцию get_tomorrow_date(), которая возвращает объект date,
# представляющий завтрашнюю дату относительно текущей даты.

from datetime import datetime, date, time, timedelta


def get_tomorrow_date(today: date) -> date:
    tomorrow = datetime.today() + timedelta(days=1)
    print(tomorrow.strftime("%a, %d %b %y"))  # Сокр.ДеньНедели, День Сокр.Месяца Год (Thu, 26 Oct 23)


get_tomorrow_date(today=date.today())
# TODO: напишите тесты для функции, используя оператор assert
