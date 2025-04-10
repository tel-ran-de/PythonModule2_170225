# Дан готовый код
# def add_prefix(text):
#   return "prefix_" + text


items = ["one", "two", "three"]
# prefixed_items = list(map(add_prefix, items))
prefixed_items = list(map(lambda x: "prefix_" + x, items))
print(prefixed_items)

# Задача: перепишите код, используя lambda-функцию
