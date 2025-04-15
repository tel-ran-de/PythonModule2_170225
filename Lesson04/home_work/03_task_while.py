
n = int(input("n:"))

i = 1
while i <= n:
    j = 1
    while j <= n:
        print(f"{i * j:4}", end=" ")
        j += 1
    print()
    print()
    i += 1