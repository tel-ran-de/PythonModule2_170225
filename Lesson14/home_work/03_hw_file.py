n = int(input("n: "))
max_len = 2 * n
line = "**"
print(f"{line:^{max_len}}")
with open("data/pyramid.txt", "w") as f:
    for i in range(n):
        f.write(f"{line:^{max_len}}\n")
        line += "**"
f.close()
