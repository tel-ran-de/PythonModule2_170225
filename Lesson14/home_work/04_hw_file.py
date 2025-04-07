import os


def russ_alphabet():
    return list(map(chr, range(ord('А'), ord('Я') + 1)))


fruits_by_letter = {}

if os.path.exists("data/fruits.txt"):

    with open("data/fruits.txt", 'r', encoding='utf-8') as f:
        for line in f:

            fruit = line.strip()

            if fruit:
                first_letter = fruit[0].upper()

                if 'А' <= first_letter <= 'Я':
                    fruits_by_letter.setdefault(first_letter, []).append(fruit)
else:
    print("Файл 'data/fruits.txt' не найден.")
    exit()

os.makedirs("fruits_files", exist_ok=True)

for letter, fruits in fruits_by_letter.items():
    file_name = f"fruits_files/fruits_{letter}.txt"

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write('\n'.join(fruits))
