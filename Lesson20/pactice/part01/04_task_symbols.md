## "Песочные часы символами"

### Задание

Дано целое положительное число `rows`, определяющее количество строк в верхней (и нижней) части "треугольников", образующих песочные часы. Написать функцию, которая выводит в терминал изображение песочных часов, состоящих из символов `*`.

### Формат входных данных

Дано целое число `rows`. `2 <= rows <= 15`.

### Формат выходных данных

Вывести изображение песочных часов, состоящее из символов `*` (см. примеры).

#### Примеры

rows = 4
```
*******
 *****
  ***
   *
  ***
 *****
*******
```
rows = 2
```
***
 *
***
```
### Решение задачи

```python
def print_rhombus_outline(rows: int):
  for i in range(rows - 1, -1, -1):
   spaces_outside = rows - 1 - i
   spaces =  2 * i + 1
   if i != 0:
    print(" " * spaces_outside + "*" * spaces)

  for i in range(rows):
   spaces_outside = rows - 1 - i
   if i == 0:
    print(" " * spaces_outside + "*")
   else:
    spaces = 2 * i + 1
    print(" " * spaces_outside + "*" * spaces)


rows = int(input("2 <= rows <= 15: "))

print_rhombus_outline(rows)
```
