# Используя функцию average() из предыдущей задачи, найдите среднее арифметическое всех элементов списка и кортежа

def average(*args):
    print(f"{args=}")
    return sum(args) / len(args)

def gen_list(size, at=-10, to=10):
    import random  # импорт в функции возможен, но не рекомендуется PEP-8
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to 
    """
    result_list = []
    for _ in range(size):
        result_list.append(random.randint(at, to))
    return result_list

my_list = gen_list(5)
print(my_list)

result = average(*my_list)
# result = average(*[1, 3, 10, -8, -5])
# result = average(1, 3, 10, -8, -5)
print(result)

# ([1, 3, 10, -8, -5],) -> (1, 3, 10, -8, -5)