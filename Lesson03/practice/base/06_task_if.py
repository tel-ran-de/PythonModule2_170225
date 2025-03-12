a = int(input("A:"))
b = int(input("B:"))
c = int(input("C:"))

if a+b > c and b+c > a and c+a > b:
    print("Существует")
else:
    print("несуществует")
