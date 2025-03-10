# Дан произвольный текст.
# Посчитайте количество символов пунктуации.
# Символами пунктуации считать .(точку) ,(запятую) и !(воскл.знак)


text = """Note that Processing now lets you call text() without first specifying a PFont with textFont(). 
In that case, a generic sans-serif font will be used instead! (See the third example above.)"""

print(text.count('.') + text.count(',') + text.count('!'))
