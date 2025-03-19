text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"

words = text.split(" ")

num_long_word = 0
for word in words:
    if len(word) > 5:
        num_long_word += 1

print(num_long_word)