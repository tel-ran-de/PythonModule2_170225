from itertools import count

n = int(input("n:"))

count = 0

while n > 0:
    number = int(input("number:"))
    if number > 0:
        count += 1
    n -= 1

print(count)