# Дан список целых чисел и число k.
# Найти максимальную сумму последовательных элементов списка длины k.
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
