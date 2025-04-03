## "Кассовый аппарат"

### Задание
Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.

По окончанию рабочей недели имеем файл [data/sold.txt](data/sold.txt). \
Товары проданные в один день аппарат записывает на одной строке.

Узнайте:
1. На какую сумму было продано товаров
2. Цену самого дорогого товара
3. Цену самого дешевого товара

### Формат входных данных

Дан текстовый файл. На каждой строке записаны числа(целые или десятичные) разделенные одним или более пробелами.

Количество строк в файле произвольное.

### Формат выходных данных

Вывести:
1. На какую сумму было продано товаров
2. Цену самого дорогого товара
3. Цену самого дешевого товара

### Решение задачи

```python
# Совет: сначала считайте все цены из файла, сохраните в список,
# преобразовав каждую цену к числу(цены в файле хранятся в виде строк)
# А затем, работам с привычным списком, выполните задания
prices = []
```
## "Кассовый аппарат"

path = "data/sold.txt"
total_sales_amount = 0.0
most_expensive_item_price = 0.0 # max
cheapest_item_price = 10000.0 # min
day = 0
with open(path, 'r', encoding='UTF-8') as file:
    for line in file:
        day += 1
        numbers_str = line.split()
        numbers_day = [float(x) for x in numbers_str]
        min_value = min(numbers_day)  # Найти минимальное значение
        max_value = max(numbers_day)  # Найти максимальное значение
        total_sales_amount += sum(numbers_day)
        print(f"day {day} price min = {min_value}, price max = {max_value}")
        most_expensive_item_price
        if min_value < cheapest_item_price:
            cheapest_item_price = min_value
        if max_value > most_expensive_item_price:
            most_expensive_item_price = max_value
print("--------------")
print(f"Цену самого дорогого товара = {most_expensive_item_price} grn")
print(f"Цену самого дешевого товара = {cheapest_item_price} grn")
print(f"total_sales_amount = {total_sales_amount} grn")
---

### Подсказки

<details>
<summary>Подсказка-1</summary>
Для преобразования строки в список вспомните про метод строки .split()

```python
line = "2 4 6 8"
numbers_str = line.split()  # numbers_str = ["2", "4", "6", "8"]
```
</details>

<details>
<summary>Подсказка-2</summary>
Самый простой способ, для преобразования списка строк к списку чисел:

```python
numbers_str = ["2", "4", "6", "8"]
numbers = []
# Пройтись по списку строк:
for el in numbers_str:
    # Каждый элемент списка преобразовать к строке
    number = int(el)
    # и добавить его в новый список
    numbers.append(number)
# numbers = [2, 4, 6, 8]
```
</details>

<details>
<summary>Подсказка-3</summary>
Для объединения списков можно воспользоваться операцией +

```python
list1 = [2, 4, 6]
list2 = ["p", "l"]
list1 += list2  # list1 = [2, 4, 6, "p", "l"]
```
</details>

<details>
<summary>Подсказка-4</summary>
Можете воспользоваться встроенными функциями или написать алгоритмы самостоятельно:

**sum(prices)** - сумма элементов списка prices \
**max(prices)** - максимальный элемент списка \
**min(prices)** - минимальные элемент списка \
</details>
