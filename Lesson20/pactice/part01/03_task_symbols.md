## "Равнобедренный треугольник символами (контур)"

### Задание

Дана высота равнобедренного треугольника. Вывести его контур символами `/`, `\` и `_`.

### Формат входных данных

Дано целое число `height`, высота треугольника. `2 <= height <= 15`.

### Формат выходных данных

Вывести контур равнобедренного треугольника, состоящий из символов `/`, `\` и `_` (см. примеры).

#### Примеры

height = 4
```
   /\
  /  \
 /    \
/______\
```
height = 3
```
  /\
 /  \
/____\
```
### Решение задачи

```python
def print_rhombus_outline(height: int):
    for i in range(height):
        spaces_outside = height - 1 - i
        if i == 0:
            print( " "* spaces_outside + "/" + "\\") #
        elif i == height - 1 :
            spaces_inside = 2 * i
            print("/" + "_" * spaces_inside + "\\")
        else:
            spaces_inside = 2 * i
            print(" "* spaces_outside + "/" + " " * spaces_inside + "\\")


height = int(input("2 <= height <= 15: "))

print_rhombus_outline(height)
```
