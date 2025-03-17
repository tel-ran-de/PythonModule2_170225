# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]
Work
import random

list_size = int(input("List :"))
numbers = []
for _ in range(list_size):
   numbers.append(random.randint(-25, 25))

result = []

for num in numbers:
   if num >= 0 :
       a = num ** 0.5
       if a % 1 == 0 :
        result.append(int(a))

print(numbers)
print(result)




main
