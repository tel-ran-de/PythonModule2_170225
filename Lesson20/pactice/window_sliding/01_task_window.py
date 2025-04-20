# Дан список целых чисел и число k.
# Найти максимальную сумму последовательных элементов списка длины k.
<<<<<<< HEAD
def get_maxsum(a, k):
    left = 0
    right = k - 1
    max_sum = 0
    while right < len(a):
        window = a[left:right + 1]

        print(window)
        elements = sum(window)
        if elements > max_sum:
            max_sum = elements
        left += 1
        right = right + 1

    return max_sum


k = 3

assert (get_maxsum([1, 23, 45, 6, 4, 22], 3)) == 74
=======

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
>>>>>>> abc6f5ff0e2b20d44f736240634f8321d0bfa1a5
