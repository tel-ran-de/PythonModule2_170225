# Дан отсортированный список целых чисел и число target.
# Найти два числа в списке, сумма которых равна target.
# Если нет пары чисел равных target, найдите пару, сумма которых максима

a = [2, 4, 6, 8, 11, 14, 23, 25]
target = 22

left = 0
right = len(a) - 1
close_numbers = a[0] + a[-1]
while True:
    summa = a[left] + a[right]
    if summa == target or left == right:
        break
    elif summa > target:
        if abs(summa - target) < abs(close_numbers - target):
            close_numbers = summa
            left += 1
    else:
        right -= 1
    if left != right:

        print(a[left], a[right])
    else:
        print("РЕШЕНИЕ НЕ НАЙДЕНО")
