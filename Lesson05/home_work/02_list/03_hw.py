# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random

n = 8
numbers = [random.randint(-100, 100) for _ in range(n)]
sum_posit_num = sum(num for num in numbers if num > 0 and num % 2 == 0)

print("список n: ", numbers)
print("сумму всех n: ", sum_posit_num)
