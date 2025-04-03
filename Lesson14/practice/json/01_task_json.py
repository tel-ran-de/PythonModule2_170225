import json


def read_json_data(filepath):
    with open(filepath, "r") as f:
        return json.load(f)


filepath = "data.data.json"
data = read_json_data(filepath)

if "name" in data:
    print(data["name"])
else:
    print("Ключ 'name' не найден в данных.")
