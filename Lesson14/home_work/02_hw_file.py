with open("data/info.txt", "r") as f:
    total = 0
    for line in f:
        line = line.strip()
        if (line.isdigit()) or (line[0] == "-" and line[1:].isdigit()):
            total += int(line)

print(f"Сумма чисел = {total}")
