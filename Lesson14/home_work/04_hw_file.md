## "Обработка списка фруктов"

### Задание

Дан файл [data/fruits.txt](data/fruits.txt) со списком фруктов. \
Записать в новые файлы все фрукты, начинающиеся с определенной буквы. \
Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д. \
Файлы назвать соответственно.
Пример имен файлов: fruits_А.txt, fruits_Б.txt, fruits_В.txt …. \
Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв, а также есть пустые строки, которые нужно пропустить. \
**Не гарантируется**, что фрукты идут по алфавиту. Т.е. сначала может быть фрукт на букву "В", а потом идти на букву "Б" \
Напишите универсальный код, который будет работать с любым списком фруктов и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.

### Формат входных данных

Дан текстовый файл, на каждой строке которого или название фрукта, или пустая строка.

### Формат выходных данных

Записать названия фруктов в разные файлы в соответствии с условием задачи.

### Решение задачи
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
                # fruits_from_file.append(line.strip())
        # print(fruits_from_file)
        for abc in list(map(chr, range(ord('А'), ord('Я') + 1))):
            # print(f"++++++abc = {abc}+++++++")
            for fruit in fruits_from_file:
                if fruit[0] == abc:
                    # print(f"fruit = {fruit}")
                    fruits_str_to_file += fruit
            # print(f"abc={abc}, fruit={fruits_str_to_file}")
            if len(fruits_str_to_file) > 0:
                with open(dir_out / f"fruits_{abc}.txt", "w", encoding="UTF-8") as f:
                    f.write(fruits_str_to_file)
            fruits_str_to_file = ""


sort_fruits()

### Подсказки

<details>
<summary>Подсказка-1</summary>
Возможно пригодится:

Чтобы получить список больших букв русского алфавита:
```python
print(list(map(chr, range(ord('А'), ord('Я')+1))))
```

</details>
