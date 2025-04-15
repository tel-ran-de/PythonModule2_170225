from datetime import datetime

date_string1 = "2024-02-15"
date_object1 = datetime.strptime(date_string1, "%Y-%m-%d").date()
print(f"Строка в дату: {date_object1}")

datetime_string2 = "2023/11/01 10:30:00"
datetime_object2 = datetime.strptime(datetime_string2, "%Y/%m/%d %H:%M:%S")
print(f"Строка в datetime: {datetime_object2}")

time_string3 = "18:05"
time_object3 = datetime.strptime(time_string3, "%H:%M").time()
print(f"Строка во время: {time_object3}")

datetime_string4 = "Oct 27, 2023 at 09:15 AM"
datetime_object4 = datetime.strptime(datetime_string4, "%b %d, %Y at %I:%M %p")
print(f"Еще одна строка в datetime: {datetime_object4}")