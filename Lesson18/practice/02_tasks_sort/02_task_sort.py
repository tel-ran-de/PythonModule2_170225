# Сумма из диапазона
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа А, но меньше B.

numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
a = float(input("a: "))
b = float(input("b: "))

sum_a = sum(x for x in numbers if x > a)
print("сумма элементов больше a :", sum_a)

sum_b = sum(x for x in numbers if x < a)
print("сумма элементов меньше чем b :", sum_b)
