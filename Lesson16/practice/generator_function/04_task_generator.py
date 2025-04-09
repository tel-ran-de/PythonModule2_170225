# Задача "Генератор степеней двойки"
# Напишите генераторную функцию powers_of_two(n), которая генерирует первые n степеней двойки (2⁰, 2¹, 2², ... 2^(n-1)).

def powers_of_two(n):
    for i in range(n):
        yield 2 ** i


n = int(input("n: "))
powers = powers_of_two(n)
print(next(powers))
print(next(powers))
print(next(powers))
print(next(powers))
print(next(powers))
