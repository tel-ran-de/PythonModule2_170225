# Задача "Генератор степеней двойки"
# Напишите генераторную функцию powers_of_two(n), которая генерирует первые n степеней двойки (2⁰, 2¹, 2², ... 2^(n-1)).

def powers_of_two(n):
    for i in range(n):
        yield i ** 2

for num in powers_of_two(4):
    print(num)
