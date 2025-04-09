import json
from pathlib import Path

# Задача: Прочитайте информацию из файлов json_data01.json ... json_data06.json
# Выведите названия файлов, содержащих некорректный JSON(с ошибками)

file_names = ['json_data01.json', 'json_data02.json', 'json_data03.json',
              'json_data04.json', 'json_data05.json', 'json_data06.json']

path = Path("data")

for file_name in file_names:
<<<<<<< HEAD
    with open(path / file_name, "r", encoding="utf-8"
              ) as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:

            print(f"Файл {file_name}")
=======
    with open(path / file_name, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            print(f"Файл {file_name} содержит некорректный JSON")
>>>>>>> 6defc2976e31c90e2919ec1b8f35a104ee59242d
