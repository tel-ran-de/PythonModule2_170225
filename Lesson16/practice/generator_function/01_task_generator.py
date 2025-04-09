# Задача "Генератор четных чисел"
# Напишите генераторную функцию even_numbers(n), которая генерирует все четные числа от 0 до n включительно.

def even_numbers(n):
    for number in range(0, n + 1, 2):
        yield number


for el in even_numbers(11):
    print(el)
