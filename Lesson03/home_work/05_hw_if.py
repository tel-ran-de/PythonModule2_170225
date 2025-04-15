a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a, b, c)
