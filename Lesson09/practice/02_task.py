# Напишите функцию, которая принимает список чисел и возвращает сумму квадратов этих чисел.

def sqrt(number):
    return number * number

numbers = [4, 6, 2, -5, 10, 3]

res = sum(map(sqrt, numbers))
print(res)