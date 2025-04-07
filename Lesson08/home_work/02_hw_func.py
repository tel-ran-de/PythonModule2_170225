# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # TODO: тело, которое вы реализовали на практической работе
xa , ya = 1, 1
xb , yb = 10, 1
xc , yc = 10, 10

leight_AB = distance(xa, ya, xb, yb)
leight_BC = distance(xb, yb, xc, yc)
leight_AC = distance(xa, ya, xc, yc)

min_leight = min(leight_AB, leight_BC, leight_AC)

if min_leight == leight_AB:
    min_leight_name = "AB"
elif min_leight == leight_BC:
    min_leight_name = "BC"
else:
    min_leight_name = "AC"

print("Самый короткий отрезок :",min_leight_name)




# TODO: your
