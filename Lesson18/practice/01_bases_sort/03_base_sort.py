# Все алгоритмы сортировки из examples/ оберните в функции


def bubble_sort(nums):
    nums = []
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return


bubble_sort()


def sort_choice(nums: list) -> None:
    nums = [5, 2, -1, 8, 4, -4, 7]

    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1
        return


sort_choice()


def quick_sort(nums):
    def partition(nums, low, high):
        # Выбираем средний элемент в качестве опорного
        # Также возможен выбор первого, последнего
        # или произвольного элементов в качестве опорного
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1

            j -= 1
            while nums[j] > pivot:
                j -= 1

            if i >= j:
                return j

            # Если элемент с индексом i (слева от опорного) больше, чем
            # элемент с индексом j (справа от опорного), меняем их местами
            nums[i], nums[j] = nums[j], nums[i]

        # Создадим вспомогательную функцию, которая вызывается рекурсивно
        def _quick_sort(items, low, high):
            if low < high:
                # Индекс опорного элемента
                split_index = partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)

    # Проверяем, что оно работает
    nums = [22, 5, 1, 18, 99, 32, 12, 18, 5]
    print("before sort = ", nums)
    quick_sort(nums)
    print("after sort = ", nums)


# Проверяем, что оно работает


quick_sort()


# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100) -> list:
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов в диапазоне at..to 
    """
    data = []
    for in range(size):
        random.randint(at, to)
        data.append(el)


gen_list(13, 33, 44)
# протестируйте функции сортировки, используя gen_list() для создания сортируемых списков
