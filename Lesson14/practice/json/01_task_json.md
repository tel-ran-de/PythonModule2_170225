## Задание 1: Чтение данных из JSON-файла

**Описание:**

Дан JSON-файл `data/data.json` со следующим содержимым:
```json
{
  "name": "Иван",
  "age": 30,
  "city": "Москва"
}
```


Необходимо написать код на Python, который прочитает данные из файла и выведет имя человека.
```python
import json

def read_json_data(filepath):
    """Читает данные из JSON-файла и возвращает словарь."""
    ...
    return data

filepath = ...
data = read_json_data(filepath)
print(data["name"])
```