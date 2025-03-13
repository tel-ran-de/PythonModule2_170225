n = int(input("n: "))
m = int(input("m: "))
k = int(input("k: "))

if (k % n == 0 or k % m == 0) and k < n * m:
    print("Yes")
else:
    print("No")