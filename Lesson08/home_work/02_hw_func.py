# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)



def find_shortest_segment(xa, ya, xb, yb, xc, yc):
    ab_distance = distance(xa, ya, xb, yb)
    bc_distance = distance(xb, yb, xc, yc)
    ac_distance = distance(xa, ya, xc, yc)
    print(f"type(ab_distance) : {type(ab_distance)}")
    print(f"bc_distance : {bc_distance}")
    min_distance = min(ab_distance, bc_distance, ac_distance)

    if min_distance == ab_distance:
        return "AB"
    elif min_distance == bc_distance:
        return "BC"
    else:
        return "AC"


xa = 1
ya = 2
xb = 4
yb = 6
xc = 7
yc = 1

shortest_segment = find_shortest_segment(xa, ya, xb, yb, xc, yc)


print("Самый короткий отрезок:", shortest_segment) 
