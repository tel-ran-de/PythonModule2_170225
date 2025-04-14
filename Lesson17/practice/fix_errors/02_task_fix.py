# Дана функция
def max_value(*args):
    "Нахождение максимального"
    maximum = args[0]
    for arg in args:
        if maximum < arg:
            maximum = arg
    return maximum


assert max_value(1, 2, 3) == 3
assert max_value(-1, -2, -3) == -1
assert max_value(0) == 0
assert max_value(2, -2, 3, -4, 0) == 3


# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
