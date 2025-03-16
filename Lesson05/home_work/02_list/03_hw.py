# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

Work

# TODO: your code here
import random

n = int(input("n:"))

numbers = []
for _ in range(n):

    numbers.append(random.randint(-100, 100))

s = 0
for i in numbers:
    if i % 2 == 0 and i > 0:
        s += i

print("сумма всех четных положительных чисел :",s)



# TODO: your code here
main
