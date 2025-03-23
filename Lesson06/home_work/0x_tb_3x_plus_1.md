## "Гипотеза 3x + 1"

### Задание

В математике есть задача, которая называется "Гипотеза 3x + 1" или "Гипотеза Коллатца" 

Подробнее про нее можно [почитать тут](https://ru.wikipedia.org/wiki/%D0%93%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0_%D0%9A%D0%BE%D0%BB%D0%BB%D0%B0%D1%82%D1%86%D0%B0) или [посмотреть отличный ролик тут] (https://youtube.com/watch?v=QgzBDZwanWA&si=EnSIkaIECMiOmarE).

Напишите программу, которая подтверждает Гипотезу Коллатца для любого заданного целого числа.

### Формат входных данных

Дано целое положительное число.

### Формат выходных данных

Программа выводит все числа, получаемы согласно правилам гипотезы. \ 
И заканчивает свою работу, как только попадает в цикл 4 --> 2 --> 1. 

### Решение задачи

```python
number = int(input("number = "))
step = 1
print("Start")
# print(number)
while True:
    if number % 2 == 0:
        number = number // 2
        print(number)
    else:
        number = number * 3 + 1
        print(number)
    if number <= 1:
        # print(int(number))
        break
    step += 1
print("Finish")
print(f"step = {step}")
```

---


