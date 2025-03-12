

n = int(input("a :"))

summa = 0
while n >= 0:
    if n % 2 == 0:
        summa += n
    n -= 1

print(summa)