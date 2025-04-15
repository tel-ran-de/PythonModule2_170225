from pathlib import Path

import json

path = 'data/new_data.json'

data = {
    "name": "Петр",
    "age": 25,
    "city": "Санкт-Петербург"
}

with open(path, "w") as file:
    json.dump(data, "data/new_data.json", ensure_ascii=False, indent=4)
