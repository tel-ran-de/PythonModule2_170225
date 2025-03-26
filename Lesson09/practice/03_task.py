# Напишите функцию, которая принимает список чисел и возвращает новый список,
<<<<<<< HEAD
# содержащий только те числа, которые делятся на 3 без остатка
#
def lis(x):
    return x%3 == 0
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = list(filter(lis, x))#
print(y)
=======
# содержащий только те числа, которые делятся на 3 без остатка.
def mult_3(number):
    return number % 3 == 0

numbers = [4, 6, 2, -5, -9, 10, 3]
res = list(filter(mult_3, numbers))
print(res)
# numbers_3 = []
#
# for number in numbers:
#     if number % 3 == 0:
#         numbers_3.append(number)
#
# print(numbers_3)
>>>>>>> 26acaefa2974c19008732e59e9eb711ea6eb273c
