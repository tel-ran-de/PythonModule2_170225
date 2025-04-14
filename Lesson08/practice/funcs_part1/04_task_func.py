
def sum_positive(numbers):
    summa = 0
    for number in numbers:
        if number > 0:
            summa += number
    return summa

assert sum_positive([6, -4, 3, 8, 2, 0, 7]) == 26, "Ошибка: ожидаем 26"
assert sum_positive([6, -4, 3]) == 9, "Ошибка: ожидаем 9"
assert sum_positive([6, 0, 3]) == 9, "Ошибка: ожидаем 9"