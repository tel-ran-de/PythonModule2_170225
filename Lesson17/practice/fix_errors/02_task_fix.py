# Дана функция
def max_value(*args):
    "Нахождение максимального"
    maximum = 0
    for arg in args:
        if maximum > arg:
            maximum = arg
    return maximum


# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
