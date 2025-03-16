# Данные о товарах на складе хранятся в словаре
from collections import Counter
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
if __name__ =="__main__":
    brands = [item["brand"] for item in items]
    all_brands = set(brands)
    
    print("Товары на складе представлены брэндами:", ', '.join(all_brands))
    count_brand = Counter(brands)

    max_count = max(count_brand.values())
    most_common = [brand for brand, count in count_brand.items() if count == max_count]
    
    max_price = max(items, key=lambda x: x["price"])
    
    print(f"На складе больше всего товаров брэнда(ов):, {', '.join(most_common)}")
    print(f"На складе самый дорогой товар брэнда(ов):, {max_price["brand"]}")
   
