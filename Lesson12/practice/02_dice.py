# Задача "Моделирование броска костей"
# Используйте функцию random.randint() для имитации броска двух игральных костей (числа от 1 до 6).
# Выведите на экран результат броска каждой кости и их сумму.
import random


def dice():
    return random.randint(1, 6)


dice_1 = dice()
dice_2 = dice()

print(dice_1, dice_2)
