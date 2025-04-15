def adder(n):
    def add(x):
        return x + n

    return add


add10 = adder(10)
print(add10(12))
