# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.
from itertools import count

a = (2,4,5)
b = (5,3,4)
c = (2,4,5)

count = 0
for element in a :
    if element in b and element in c :
        count += 1
print("количество общих элементов:",count)





tup1 = (2, 4, 6, 0)
tup2 = (-3, 4, 12, 2, 0, 5)
tup3 = (2, -4, 12, 0, 5)

count = 0
for el1 in tup1:
    if el1 in tup2 and el1 in tup3:
        count += 1

print(count)
