# У вас есть список строк.
# Вам нужно получить список длин всех строк, которые имеют длину более 3 символов.

words = ["cat", "dog", "elephant", "mouse", "bird", "ant"]

words_3 = list(filter(lambda word: len(word) > 3, words))
print(words_3)
