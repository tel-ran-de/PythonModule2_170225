from pathlib import Path

# Задача: Найти сумму всех чисел в файле 'numbers.txt', пропустив все нечисловые значения.

path = Path('data') / 'numbers.txt'

with open(path, 'r', encoding='UTF-8') as f:
    # Находим сумму всех чисел в файле
    s = 0
    for line in f:
        try:
            s += int(line)
        except ValueError:
            pass

print(s)
