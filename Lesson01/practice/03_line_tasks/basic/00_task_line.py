a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))  # Ctrl + D - дублирование строки

p = (a + b + c) / 2  # Ctrl+Alt+L - автоформат по PEP-8
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
perimeter = a + b + c

print("Площадь = ", area)
print("Периметр = ", perimeter)
