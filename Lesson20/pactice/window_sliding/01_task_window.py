# Дан список целых чисел и число k.
# Найти максимальную сумму последовательных элементов списка длины k.

def get_max_sum(numbers, k):
    left = 0
    right = k - 1
    max_sum = 0
    while right < len(numbers):
        window = numbers[left: right + 1]
        sum_elements = sum(window)
        if sum_elements > max_sum:
            max_sum = sum_elements
        left += 1
        right += 1
    return max_sum


assert get_max_sum([2, 12, 4, 26, -4, 0, 22, 1, 5, 8], 3) == 42
assert get_max_sum([2, 12, 4, 6, -4, 0, 22, 1, 5, 8], 3) == 28
assert get_max_sum([2, 12, 4, 6, -4, 0, 2, 1, 5], 3) == 22
assert get_max_sum([2, 12], 2) == 14
assert get_max_sum([2, 12], 1) == 12
