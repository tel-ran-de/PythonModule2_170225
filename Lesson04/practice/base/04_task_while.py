<<<<<<< HEAD


n = int(input("n:"))

count = 0

while n > 0:
    number = int(input("number:"))
=======
n = int(input("n: "))

count = 0
while n > 0:
    number = int(input("number: "))
>>>>>>> 0fa97f92ba32ed2252a2bb0d795ce3f64ea72362
    if number > 0:
        count += 1
    n -= 1

print(count)