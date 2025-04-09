# Задача "Генератор четных чисел"
# Напишите генераторную функцию even_numbers(n), которая генерирует все четные числа от 0 до n включительно.

def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


even = even_numbers(10)

print(next(even))
print(next(even))
print(next(even))
print(next(even))
