<<<<<<< HEAD
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
=======
from pathlib import Path
from typing import Union


def sort_fruits(in_file: Union[str, Path] = "data/fruits.txt",
                dir_out: Union[str, Path] = "data/fruits_sorted/") -> None:
    """
    Обрабатывает список фруктов из входного текстового файла и сортирует их по первой букве.
    Для каждой буквы алфавита (А–Я) создаётся отдельный файл, содержащий фрукты, начинающиеся с этой буквы.
    Аргументы:
    ----------
    in_file : str | Path
        Путь к входному файлу со списком фруктов. Один фрукт — одна строка.
    dir_out : str | Path
        Папка, в которую будут сохраняться отсортированные файлы.
    Выход:
    ------
    None. Создаёт текстовые файлы вида fruits_А.txt, fruits_Б.txt и т.д.
    """
    fruits_from_file = []
    fruits_str_to_file = ""
    dir_out = Path(dir_out)
    dir_out.mkdir(parents=True, exist_ok=True)

    with open(in_file, "r", encoding="UTF-8") as f:
        for line in f:
            if line[0] != "\n":
                fruits_from_file.append(line)
        for abc in list(map(chr, range(ord('А'), ord('Я') + 1))):
            for fruit in fruits_from_file:
                if fruit[0] == abc:
                    fruits_str_to_file += fruit
            if len(fruits_str_to_file) > 0:
                with open(dir_out / f"fruits_{abc}.txt", "w", encoding="UTF-8") as f:
                    f.write(fruits_str_to_file)
            fruits_str_to_file = ""

def sort_fruits_v2(in_file = "data/fruits.txt", dir_out = "data/fruits_sorted/"):
    dir_out = Path(dir_out)
    dir_out.mkdir(parents=True, exist_ok=True)
    with open(in_file, "r", encoding="UTF-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            letter = line[0]
            with open(dir_out / f"fruits_{letter}.txt", "a", encoding="UTF-8") as f_write:
                f_write.write(line+ "\n")

sort_fruits_v2()
>>>>>>> 6defc2976e31c90e2919ec1b8f35a104ee59242d
