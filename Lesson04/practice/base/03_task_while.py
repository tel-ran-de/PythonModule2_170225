<<<<<<< HEAD


n = int(input("a :"))
=======
n = int(input("n: "))
>>>>>>> 0fa97f92ba32ed2252a2bb0d795ce3f64ea72362

summa = 0
while n >= 0:
    if n % 2 == 0:
        summa += n
    n -= 1

print(summa)