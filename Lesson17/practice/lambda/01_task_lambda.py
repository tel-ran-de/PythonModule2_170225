# Дан готовый код
# def is_even(n):
<<<<<<< HEAD
#    return n % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# even_numbers = list(filter(is_even, numbers))
=======
#     return n % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
>>>>>>> 68b338dc43d0d6145b3c52e09c1e88e0928f2085
print(even_numbers)

# Задача: перепишите код, используя lambda-функцию
