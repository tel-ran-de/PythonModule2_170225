# Совет: сначала считайте все цены из файла, сохраните в список,
# преобразовав каждую цену к числу(цены в файле хранятся в виде строк)
# А затем, работам с привычным списком, выполните задания
prices = []
path = "data/sold.txt"
with open(path, 'r') as file:
    for line in file:
        prices += (line.split())

print(prices)
prices_number = list(map(float, prices))
print(sum(prices_number))
print(max(prices_number))
print(min(prices_number))
