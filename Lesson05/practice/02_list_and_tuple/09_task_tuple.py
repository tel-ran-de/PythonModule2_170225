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





# TODO: your code here
