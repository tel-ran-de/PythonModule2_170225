summa = 0
with open("data/info.txt", "r", encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        if line.lstrip("-").isdigit() and line.count("-") <= 1 and line.find("-") in (0, -1):
            summa += int(line)
            print(line)

print(f"Сумма чисел = {summa}")

# Уточнение: в сумму добавляем только те значения, которые можно преобразовать к int'у
# Например: int("-26") --> -26, а int("--26") --> ошибка
