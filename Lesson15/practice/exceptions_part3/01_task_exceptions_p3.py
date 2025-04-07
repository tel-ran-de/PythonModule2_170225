import json
from pathlib import Path


def parse_json_file(filename):
    with open(filename, "r") as f:
        return json.load(f)


def process_json_data(filename):
    data = parse_json_file(filename)
    return data[0]

# Задача: выполните предложенные код со всеми файлами json_data01.json ... json_data06.json
# Обратите внимание, для каких файлов срабатывает какая обработка исключения

try:
    process_json_data(Path("data") / "json_data0x.json")
except FileNotFoundError:
    print("Файл не найден!")
except json.JSONDecodeError as e:
    print(f"Ошибка JSON: {e}")
except KeyError:
    print(f"Некорректная обработка данных")
