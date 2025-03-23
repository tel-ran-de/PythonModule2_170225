# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

import math

def is_one_circle_inside_another(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if r1 > r2:
        return d <= r1 - r2
    else:
        return d <= r2 - r1

x1 = 0
y1 = 0
r1 = 2
x2 = 3
y2 = 4
r2 = 5

result = is_one_circle_inside_another(x1, y1, r1, x2, y2, r2)
if result:
    print("Одна окружность находится внутри другой")
else:
    print("Окружности не находятся друг в друге")
