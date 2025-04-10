# create_multiplier является функцией высшего порядка, поскольку она возвращает другую функцию (multiplier)

def create_multiplier(factor):
    """Возвращает функцию, умножающую на factor."""

    def multiplier(x):
        """Умножает x на factor."""
        return x * factor

    return multiplier


# Создаем различные функции-умножители
double = create_multiplier(2)
triple = create_multiplier(3)

# Используем созданные функции
result_double = double(10)
print(f"10 умноженное на 2: {result_double}")  # Вывод: 10 умноженное на 2: 20

result_triple = triple(10)
print(f"10 умноженное на 3: {result_triple}")  # Вывод: 10 умноженное на 3: 30
