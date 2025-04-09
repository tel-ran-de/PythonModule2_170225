# Задача "Генератор случайных целых чисел"
# Напишите генераторную функцию random_integers(n), которая генерирует n случайных целых чисел
# в диапазоне от 1 до 100 (используйте модуль random).

import random

def random_integers(n):
    for _ in range(n):
        yield random.randint(1, 100)


for num in random_integers(4):
    print(num)
