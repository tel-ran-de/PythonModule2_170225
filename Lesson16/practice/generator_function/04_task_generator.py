# Задача "Генератор степеней двойки"
# Напишите генераторную функцию powers_of_two(n), которая генерирует первые n степеней двойки (2⁰, 2¹, 2², ... 2^(n-1)).

def powers_of_two(n):
<<<<<<< HEAD
    for i in range(n):
        yield 2 ** i


n = int(input("n: "))
powers = powers_of_two(5)
print(list(powers_of_two(5)))
print(next(powers))
print(next(powers))
print(next(powers))
print(next(powers))
=======
    result = 1
    for i in range(n):
        yield result
        result *= 2


print(list(powers_of_two(1)))
print(list(powers_of_two(2)))
print(list(powers_of_two(4)))

# 2^0 = 1
# 2^1 = 2
# 2^2 = 4
# 2^3 = 8
# 2^4 = 16
>>>>>>> d6041d05ecef6a9912aa912e92a67475e5be03d6
