## "Подсчет длинных слов"

### Задание

Определить в предоставленном сообщении количество слов длиной больше, чем 5.

### Формат входных данных

Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.

### Формат выходных данных

Вывести количество найденных слов.

### Решение задачи

```python
text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"

worter = text.split()

wortlange = [word for word in worter if len(word) > 5]

zahl_worter= len(wortlange)

print("Anzahl der Wörter mit mehr als 5 Zeichnen:", zahl_worter)
```

---

