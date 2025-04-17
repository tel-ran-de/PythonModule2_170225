# Дан отсортированный список целых чисел и число target.
# Найти два числа в списке, сумма которых равна target.
# Гарантируется, что в списке если пара, сумма которых равна target

numbers = [4, 5, 8, 12, 14, 22, 25]
target = 22

left = 0
right = len(numbers) - 1

while True:
    summa = numbers[left] + numbers[right]
    if summa == target:
        break
    elif summa < target:
        left += 1
    else:
        right -= 1

print(numbers[left], numbers[right])
