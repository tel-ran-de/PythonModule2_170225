# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

numbers = []
sum_number = 0

print("введите в диапазоне от -100 до 100")

while True:
    n = int(input("ввод: "))
    if -100 <= n <= 100:
        break
while n > 0:
    number = random.randint(-100, 100)
    numbers += [number]
    n -=1
for number in numbers:
    if number > 0 and number%2 == 0:
        sum_number += number

print(numbers)
print(sum_number)
