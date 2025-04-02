# Задача "Моделирование броска костей"
# Используйте функцию random.randint() для имитации броска двух игральных костей (числа от 1 до 6).
# Выведите на экран результат броска каждой кости и их сумму.
import random

def dice_roll():
    return random.randint(1, 6)


dice1 = dice_roll()
dice2 = dice_roll()

print(dice1, dice2)
