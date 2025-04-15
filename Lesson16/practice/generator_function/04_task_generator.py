# Задача "Генератор степеней двойки"
# Напишите генераторную функцию powers_of_two(n), которая генерирует первые n степеней двойки (2⁰, 2¹, 2², ... 2^(n-1)).

def powers_of_two(n):
    for i in range(n):
        yield 2 ** i


n = int(input("n: "))
powers = powers_of_two(5)
print(list(powers_of_two(5)))
print(next(powers))
print(next(powers))
print(next(powers))
print(next(powers))

# Removed duplicated code block from here as it was unnecessary


print(list(powers_of_two(1)))
print(list(powers_of_two(2)))
print(list(powers_of_two(4)))

# 2^0 = 1
# 2^1 = 2
# 2^2 = 4
# 2^3 = 8
# 2^4 = 16
