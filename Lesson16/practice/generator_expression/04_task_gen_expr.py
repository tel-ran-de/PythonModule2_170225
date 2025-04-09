# "Буквы верхнего регистра из строки"
# Генераторное выражение, возвращающее все буквы верхнего регистра из заданной строки.

string = "Hello WorLd"

upper_gen = (char for char in string if char.isupper())
print(list(upper_gen))