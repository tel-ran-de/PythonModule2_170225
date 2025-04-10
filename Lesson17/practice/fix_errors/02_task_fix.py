# Дана функция
def max_value(*args):
    "Нахождение максимального"
    maximum = args[0]
    for arg in args:
        if maximum < arg:
            maximum = arg
    return maximum


def test_max_value():
    assert max_value(1, 2, 3) == 3
    assert max_value(1, 2, 3, 4) == 4
    assert max_value(1, 2, 3, 4, 5) == 5


test_max_value()
# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
