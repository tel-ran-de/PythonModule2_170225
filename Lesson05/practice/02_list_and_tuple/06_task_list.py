# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

start = min(first_number, second_number)
end = max(first_number, second_number)

n = start
print ("числа кратные трем : ")

while  n <= end:
    if n % 3 == 0:
      print(n)
    n += 1
# TODO: your code here
