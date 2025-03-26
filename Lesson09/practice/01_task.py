# Напишите функцию, которая принимает список строк и возвращает новый список,
# где каждая строка преобразована в верхний регистр.

strings = ["hello", "world", "my", "age"]

def to_upper_case(string):
    return string.upper()

# Вариант-1:
# upper_strings = []
# for string in strings:
#     upper_strings.append(string.upper())

# Вариант-2:
# upper_strings = [string.upper() for string in strings]

# Вариант-3:
upper_strings = list(map(to_upper_case, strings))

print(upper_strings)