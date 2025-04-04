from pathlib import Path
import json


def read_json_data(filepath):
    """Читает данные из JSON-файла и возвращает словарь."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


filepath = Path('data/data.json')
data = read_json_data(filepath)
print(data["age"])
