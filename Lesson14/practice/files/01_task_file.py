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
