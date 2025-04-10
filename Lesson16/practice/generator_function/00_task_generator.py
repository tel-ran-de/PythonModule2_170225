# "Генератор простых чисел":
# Напишите генераторную функцию simple_primes(n), которая генерирует простые числа до n

def is_prime(n: int) -> bool:
    """
    Проверяет, является ли заданное целое число простым.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def simple_primes(n):
    for number in range(n + 1):
        if is_prime(number):
            yield number


for prime in simple_primes(30):
    print(prime)