## "Диагонали символами"

### Задание

Даны сторона квадрата. Вывести его диагонали символами #

### Формат входных данных

Дано целое число n, длина стороны квадрата. 3 < n < 20 

### Формат выходных данных

Вывести диагонали квадрата символами # (см. примеры)

#### Примеры

n = 6 
```
#    #
 #  #
  ##
  ##
 #  #
#    #
```
n = 3
```
# #
 #
# #
```
### Решение задачи

```python
n = int(input("3 < n < 20: "))
# n = 8
side = int(n/2)

for i in range(side, 0, -1):
    spaces_outside = side - i
    spaces = 2 * i -1
    print(" " * spaces_outside + "#" + " " * spaces + "#")
    if n % 2 != 0 and i == 1:
        print(" " * (spaces_outside+1) + "#")

for i in range(1, side + 1):
    spaces_outside = side - i
    spaces = 2 * i - 1
    print(" " * spaces_outside + "#" + " " * spaces + "#")
```
