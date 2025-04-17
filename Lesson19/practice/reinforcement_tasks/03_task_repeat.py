# "Генератор простых чисел до определенного значения"
#
# Входные данные: Целое положительное число n.
# Результат: Генератор, выдающий простые числа до n.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_numbers_up_to(n):
    """
    Генератор, выдающий простые числа до n.
    """
    for i in range(1, n + 1):
        if is_prime(i):
            yield i
<<<<<<< HEAD
    return
=======
>>>>>>> 313dbff6d8a5cacc923f6a78edd0509c9d16bad3

# Пример использования:
# for prime in prime_numbers_up_to(20):
#     print(prime) # Ожидаемый вывод: 2 3 5 7 11 13 17 19
