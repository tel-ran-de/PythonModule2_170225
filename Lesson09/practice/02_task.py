# Напишите функцию, которая принимает список чисел и возвращает сумму квадратов этих чисел.
def sum_squares(digits):
    suma = 0
    for digit in digits:
        suma += digit ** 2
        return suma

digits = [2, 3]
print(sum_squares(digits))
