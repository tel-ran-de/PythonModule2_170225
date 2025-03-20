# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:
import math
def point_in_circle(x, y, xc, yc, r):
    # TODO: your code here
    centr = math.sqrt((x - xc) ** 2 + (y - yc) ** 2)

    return centr < r

# Не забудьте протестировать вашу функцию
