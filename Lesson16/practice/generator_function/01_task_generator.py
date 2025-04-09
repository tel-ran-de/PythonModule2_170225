# Задача "Генератор четных чисел"
# Напишите генераторную функцию even_numbers(n), которая генерирует все четные числа от 0 до n включительно.

def even_numbers(n):
    for even in range(n):
        if even % 2 == 0:
            yield even

for num in even_numbers(10):
    print(num)
