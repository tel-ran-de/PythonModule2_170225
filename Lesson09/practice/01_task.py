# Напишите функцию, которая принимает список строк и возвращает новый список,
# где каждая строка преобразована в верхний регистр.
<<<<<<< HEAD
from ctypes import HRESULT
from idlelib.debugger_r import restart_subprocess_debugger

strings = ["hello", "word", "my", "age"]
#upper_strings =[]

# Вариант 1
#for string in strings:
  # upper_strings.append(string.upper())

#print(upper_strings)

#Вариант 2

#upper_strings = [string.upper() for string in strings]

#print(upper_strings)

#3 Вариант

def count_upper(strings):
    count = 0
    for string in strings:
        if string.isupper():
            count += 1
    return count


result = count_upper(strings)
print(result)
=======

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
>>>>>>> 26acaefa2974c19008732e59e9eb711ea6eb273c
