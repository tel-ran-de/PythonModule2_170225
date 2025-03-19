# n = 4

# 1 2 3 4 x1
# 2 4 6 8 x2
# 3 6 9 12 x3
# 4 8 12 16 x4

n = int(input("n: "))

j = 1
line = ""
while j <= n:
    i = 1
    while i <= n:
        line += str(i * j) + " "  # 1 -> "1 2 3 4 "
        i += 1
    print(line)
    line = ""
    j += 1
