from pathlib import Path
import pickle

DIR = 'files'
python_data = [{"name": 'Петр', 'age': 10}, {"name": 'Александр', 'age': 8}]

# Записываем объект Python в файл в виде бинарника
path = Path(DIR) / 'save_pickle_data'
path.parent.mkdir(parents=True, exist_ok=True) # Создаем директорию, если она не существует.
with path.open('wb') as f:
    pickle.dump(python_data, f)

# Читаем данные их файла и преобразуем к типу Python (восстанавливаем объект из файла)
with path.open('rb') as f:
    read_data = pickle.load(f)

print(read_data)
print(read_data[0])