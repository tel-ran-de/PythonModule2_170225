from pathlib import Path
import json

DIR = 'files'
python_data = [{"name": 'Петр', 'age': 10}, {"name": 'Александр', 'age': 8}]

# Записываем объект Python в файл в виде JSON
path = Path(DIR) / 'save_json_data.json'
path.parent.mkdir(parents=True, exist_ok=True)  # Создаем директорию, если она не существует.
with open(path, 'w', encoding='UTF-8') as file:
    json.dump(python_data, file, ensure_ascii=False, indent=4)
    # ensure_ascii=False - чтобы некирилические символы не были преобразованы к unicode-последовательности
    # indent=4 - форматирование отступами в 4 пробела

# Читаем JSON из файла и преобразуем к типу Python
with open(path, 'r', encoding='UTF-8') as f:
    read_data = json.load(f)

print("type = ", type(read_data))
print("data = ", read_data)

# Плюсы: Легко читаемая и редактируемая информация в файле
#        JSON можно передавать различным программам на других языках
# Минусы: К JSON можно преобразовать далеко не все стандартные объекты python
