text = "мАма мЫла раму"
vowels = "ауоыэяюёие"

num_vowels = 0
for char in text.lower():
    if char in vowels:
        num_vowels += 1

print(num_vowels)