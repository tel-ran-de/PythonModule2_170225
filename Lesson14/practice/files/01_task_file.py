<<<<<<< HEAD
path = "data/numbers.txt"

f = open(path, "r")
sum_numbers = 0
count = 0
for line in f:
    sum_numbers += int(line)

    count += 1

f.close()

print(f"Сумма чисел = {sum_numbers}")
print(f"Среднеарифметическое = {sum_numbers / count}")
=======
# Задаем путь к файлу:
path = "data/numbers.txt"  # вместо dir подставь название папки с файлом.
# Или удалите dir, если numbers.txt в той же папке, что и питоновский файл

# Открываем файл на чтение
f = open(path, "r")
sum_numbers = 0  # Переменная для подсчета суммы
count = 0
# В переменную line считываем строку за стройкой из файла(f)
for line in f:
    sum_numbers += int(line)
    count += 1

f.close() # Закрываем файл
print(f"Сумма чисел = {sum_numbers}")
print(f"Среднеарифметическое = {sum_numbers/count}")
>>>>>>> 0e5eb8b83fc330f0251cd13e3b23733541763246
