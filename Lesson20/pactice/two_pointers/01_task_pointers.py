# Дан отсортированный список целых чисел и число target.
# Найти два числа в списке, сумма которых равна target.
# Гарантируется, что в списке если пара, сумма которых равна target

<<<<<<< HEAD

a = [2, 4, 6, 8, 11, 14, 23, 25]
target = 22

left = 0
right = len(a) - 1

while True:
    summa = a[left] + a[right]
=======
numbers = [4, 5, 8, 12, 14, 22, 25]
target = 22

left = 0
right = len(numbers) - 1

while True:
    summa = numbers[left] + numbers[right]
>>>>>>> abc6f5ff0e2b20d44f736240634f8321d0bfa1a5
    if summa == target:
        break
    elif summa < target:
        left += 1
    else:
        right -= 1
<<<<<<< HEAD
    print(a[left], a[right])
=======

print(numbers[left], numbers[right])
>>>>>>> abc6f5ff0e2b20d44f736240634f8321d0bfa1a5
