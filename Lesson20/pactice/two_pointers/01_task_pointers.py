# Дан отсортированный список целых чисел и число target.
# Найти два числа в списке, сумма которых равна target.
# Гарантируется, что в списке если пара, сумма которых равна target


a = [2, 4, 6, 8, 11, 14, 23, 25]
target = 22

left = 0
right = len(a) - 1

while True:
    summa = a[left] + a[right]
    if summa == target:
        break
    elif summa < target:
        left += 1
    else:
        right -= 1
    print(a[left], a[right])
