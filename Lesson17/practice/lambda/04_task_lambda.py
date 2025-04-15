# Дан готовый код
# def add_prefix(text):
<<<<<<< HEAD
#   return "prefix_" + text


items = ["one", "two", "three"]
# prefixed_items = list(map(add_prefix, items))
prefixed_items = list(map(lambda x: "prefix_" + x, items))
=======
#     return "prefix_" + text


items = ["one", "two", "three"]
prefixed_items = list(map(lambda text: "prefix_" + text, items))
>>>>>>> 68b338dc43d0d6145b3c52e09c1e88e0928f2085
print(prefixed_items)

# Задача: перепишите код, используя lambda-функцию
