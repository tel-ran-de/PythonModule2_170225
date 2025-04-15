# Задача "Генерация случайного числа с плавающей точкой в заданном диапазоне"
# Задайте диапазон (например, от -10 до 10).
# Используйте функцию random.uniform() для генерации случайного числа с плавающей точкой в этом диапазоне.
# Выведите на экран сгенерированное число.
import random


def generate_number(at: int = -10, to: int = 10) -> float:
    floating_number = round(random.uniform(at, to), 2)
    return floating_number


print(generate_number())
