# Напишите функцию для расчета площади прямоугольника.
#
# Входные данные:
#   w: ширина прямоугольника.
#   h: высота прямоугольника.
# Результат:
#   площадь прямоугольника.

def calculate_rectangle_area(w, h):
    s = w*h
    print(s)
    return s




width = int(input("width = "))
height = int(input("height = "))

area = calculate_rectangle_area(width, height)
print(f"Площадь прямоугольника = {area}")
