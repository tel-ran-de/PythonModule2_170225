# Напишите функцию, которая принимает список чисел и возвращает новый список,
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