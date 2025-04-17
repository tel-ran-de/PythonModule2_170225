# Дан отсортированный список целых чисел и число target.
# Найти два числа в списке, сумма которых равна target.
# Если нет пары чисел равных target, найдите пару, сумма которых максимально близка к target.

numbers = [4, 5, 8, 12, 15, 22, 25]
target = 22

left = 0
right = len(numbers) - 1
close_numbers = numbers[0] + numbers[-1]

while True:
    summa = numbers[left] + numbers[right]
    if abs(summa - target) < abs(close_numbers - target):
        close_numbers = summa
    if summa == target or left == right:
        break
    elif summa < target:

        left += 1
    else:
        right -= 1

if left != right:
    print(numbers[left], numbers[right])
else:
    print("Решение не найдено")
    print(f"Ближайшая сумма = {close_numbers}")

# tr = 35
# cn = 50
#
# s = 40 | 38 | 34 | 32
