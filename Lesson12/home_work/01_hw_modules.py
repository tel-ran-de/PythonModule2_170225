# "Вычисление площади случайного треугольника"
# Сгенерируйте случайные координаты трех точек на плоскости.
# Используйте модуль math для вычисления длин сторон треугольника.
# Вычислите площадь треугольника, используя формулу Герона.

import math
import random

x1, y1 = random.randint(1, 10), random.randint(1, 10)
x2, y2 = random.randint(1, 10), random.randint(1, 10)
x3, y3 = random.randint(1, 10), random.randint(1, 10)


def triangle_area(x1, y1, x2, y2, x3, y3) -> float:
    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area


area = triangle_area(x1, y1, x2, y2, x3, y3)
print(f"Координаты : {x1}, {y1}, {x2}, {y2}, {x3}, {y3}")
print(f"Площадь треугольника {area}")
