# Дан список. Вывести элементы списка, пронумеровав их начиная с единицы.
# Каждый элемент должен быть выведен с новой строки.

fruits = ["яблоко", "банан", "киви", "ананас", "груша"]

<<<<<<< HEAD
Work
print("1:", fruits[0])
print("2:",fruits[1])
print("3:",fruits[2])
print("4:",fruits[3])
print("5:",fruits[4])

main
# TODO: your code here
=======
# вариант-1
# i = 0
# for fruit in fruits:
#     i = i + 1
#     print(f"{i}.{fruit}")

# вариант-2
for i, fruit in enumerate(fruits, 1):
    print(f"{i}.{fruit}")



>>>>>>> 759f5857c41c75f65deba10d03e8b7641eeb8118
