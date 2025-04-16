from datetime import datetime

now = datetime.now()

# Различные форматы даты
print(now.strftime("%Y-%m-%d"))  # Год-Месяц-День (2023-10-26)
print(now.strftime("%d/%m/%Y"))  # День/Месяц/Год (26/10/2023)
print(now.strftime("%d %B, %Y"))  # День НазваниеМесяца, Год (26 October, 2023)
print(now.strftime("%a, %d %b %y"))  # Сокр.ДеньНедели, День Сокр.Месяца Год (Thu, 26 Oct 23)

# Различные форматы времени
print(now.strftime("%H:%M:%S"))  # Час:Минута:Секунда (22:45:10)
print(now.strftime("%I:%M %p"))  # Час:Минута AM/PM (10:45 PM)

# Комбинированные форматы
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%c"))  # Предпочтительное представление даты и времени

# Подробнее про форматирование можно почитать
# тут: https://www.programiz.com/python-programming/datetime/strftime
# и тут: https://www.w3schools.com/python/python_datetime.asp