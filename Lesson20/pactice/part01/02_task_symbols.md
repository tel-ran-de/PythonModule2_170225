## "Ромб символами"

### Задание

Дана длина стороны ромба. Вывести его контур символами `+`.

### Формат входных данных

Дано целое число `side`, длина стороны ромба. `2 <= side <= 15`.

### Формат выходных данных

Вывести контур ромба, состоящий из символов `+` (см. примеры).

#### Примеры


side = 4 
```
   +
  + +
 +   +
+     +
 +   +
  + +
   +
```
side = 2
```
 +
+ +
 +
```
### Решение задачи

```python
def print_rhombus_outline(side: int):
    for i in range(side):
        spaces_outside = side - 1 - i
        if i == 0:
            print(" " * spaces_outside + "+")
        else:
            spaces_inside = 2 * i - 1
            print(" " * spaces_outside + "+" + " " * spaces_inside + "+")

    for i in range(side - 2, -1, -1):
        spaces_outside = side - 1 - i
        if i == 0:
            print(" " * spaces_outside + "+")
        else:
            spaces_inside = 2 * i - 1
            print(" " * spaces_outside + "+" + " " * spaces_inside + "+")


side = int(input("2 <= side <= 15: "))

print_rhombus_outline(side)
```
