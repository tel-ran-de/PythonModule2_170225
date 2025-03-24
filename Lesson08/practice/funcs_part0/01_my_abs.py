def my_abs(number):
    if number < 0:
        return -number
    return number

def my_abs(number):
    return number if number >= 0 else -number


print(my_abs(-5))
print(my_abs(5))
print(my_abs(0))
print(my_abs(-2.5))
print(my_abs(2.5))
