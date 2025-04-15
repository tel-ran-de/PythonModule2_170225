<<<<<<< HEAD
def my_abs(numebr):
    if numebr < 0:
     return -numebr

    return numebr


print(my_abs(-5))
print(my_abs(5))
print(my_abs(0))
print(my_abs(-2.5))
=======
def my_abs(number: int | float) -> int | float:
    if number < 0:
        return -number
    return number


my_abs(-123)
my_abs(5.6)
>>>>>>> 26acaefa2974c19008732e59e9eb711ea6eb273c
