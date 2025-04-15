nums = [5, 2, -1, 8, 4, -4, 7]
print("before sort = ", nums)

# Дан алгоритм сортировки
# TODO: Измените алгоритм, чтобы сортировка работала в обратном порядке, от большего к меньшему.

i = 0
while i < len(nums) - 1:
    m = i
    j = i + 1
    while j < len(nums):
        if nums[j] > nums[m]:
            m = j
        j += 1
    nums[i], nums[m] = nums[m], nums[i]
    i += 1

print("after sort = ", nums)
