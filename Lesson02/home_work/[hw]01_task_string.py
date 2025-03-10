# Дан произвольный текст.
# Посчитайте количество символов пунктуации.
# Символами пунктуации считать .(точку) ,(запятую) и !(воскл.знак)

text = input("Введите текст: ")

punctuation_count = text.count(".") + text.count(",") + text.count("!")

print(punctuation_count)
