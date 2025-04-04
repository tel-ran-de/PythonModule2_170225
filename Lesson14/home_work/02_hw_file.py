summa = 0
with open("data/info.txt", "r") as f:
    for line in f:
        try:
            summa += int(line)
        except ValueError:
            pass

print(f"Сумма чисел = {summa}")
# Уточнение: в сумму добавляем только те значения, которые можно преобразовать к int'у
# Например: int("-26") --> -26, а int("--26") --> ошибка
