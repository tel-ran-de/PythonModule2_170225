# Задаем путь к файлу:
path_read = "data/limericks.txt"  # вместо dir подставь название папки с файлом.
path_write = "data/limericks_clean.txt"  # вместо dir подставь название папки с файлом.
# Или удалите dir, если limericks.txt в той же папке, что и питоновский файл

# Открываем файл на чтение
f_read = open(path_read, "r", encoding="utf-8")
f_write = open(path_write, "w", encoding="utf-8")
# В переменную line считываем строку за стройкой из файла(f)
for line in f_read:
    new_line = line.replace(".", "")
    f_write.write(new_line)

f_write.close()
f_read.close()