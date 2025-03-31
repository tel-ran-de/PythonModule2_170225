def my_abs(number: int | float) -> int | float:
    if number < 0:
        return -number
    return number


my_abs(-123)
my_abs(5.6)