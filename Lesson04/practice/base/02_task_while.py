
a = int(input("a: "))
b = int(input("b: "))

# if a % 2 != 0:
#     a +=1
#
# while a <= b:
#     print(a)
#     a += 2

while a <= b:
    if a % 2 == 0:
        print(a)
    a += 1