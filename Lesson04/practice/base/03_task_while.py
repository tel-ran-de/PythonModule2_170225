


n = int(input("a :"))

n = int(input("n: "))


summa = 0
while n >= 0:
    if n % 2 == 0:
        summa += n
    n -= 1

print(summa)