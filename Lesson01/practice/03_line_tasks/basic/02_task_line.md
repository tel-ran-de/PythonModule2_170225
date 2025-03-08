## "Расстояние между точками"

### Задание

Даны координаты (x,y) двух точек на координатной плоскости. Вычислите расстояние между точками.

### Формат входных данных

Даны 4 целые числа, координаты точек

### Формат выходных данных

Вывести расстояние между точками с заданными координатами

### Решение задачи

```python
x1 = int(input("Geben Sie x1 ein: "))
x2 = int(input("Geben Sie x2 ein: "))
y1 = int(input("Geben Sie y1 ein: "))
y2 = int(input("Geben Sie y2 ein: "))

abstand = ((x2-x1)**2 +(y2-y1)**2)**0.5


print(f"Die Entfernung zwieschen den Punkten beträgt:{abstand:.1f}")
```

---

### Подсказки

<details>
<summary>Подсказка-1</summary>
Формулу расстояния между двумя точками можно легко найти в гугле
</details>

<details>
<summary>Подсказка-2</summary>
Для вычисления квадратного корня можно возвести в степень 0.5 <br>
Пример: n ** 0.5
</details>

<details>
<summary>Подсказка-3</summary>
Для проверки результата можете воспользоваться <a href="https://ru.onlinemschool.com/math/assistance/cartesian_coordinate/p_length/">онлайн калькулятором</a> 
</details>
