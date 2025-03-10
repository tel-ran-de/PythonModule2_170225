import re

text = input("Введите строку: ")

if re.fullmatch(r"id:\d+", text):
    print("Да")
else:
    print("Нет")