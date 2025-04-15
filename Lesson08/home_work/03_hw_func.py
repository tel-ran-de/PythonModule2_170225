# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here
x1 = int(input("x1 :"))
y1 = int(input("y1 :"))
x2 = int(input("x2 :"))
y2 = int(input("y2 :"))
R1 = int(input("R1 :"))
R2 = int(input("R2 :"))
if R1 <= 0 or R2 <= 0:
    print("error")
    exit()
else: dx = x2 - x1; dy = y2 - y1; distance = (dx * dx + dy * dy)

radiusdiff1 = R1 - R2
radiusdiff2 = R2 - R1

if distance <= radiusdiff1 * radiusdiff2:
    print("yes , первая внутри второй")
elif distance <= radiusdiff2 * radiusdiff1:
    print("yes, вторая внутри первой")
else:
    print("no, окружности не находятся внутри друг друга")