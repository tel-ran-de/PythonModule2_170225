text = "Посчитайте количество согласных букв в данной строке."
s = text

s = s.replace('а', '')
s = s.replace('и', '')
s = s.replace('е', '')
s = s.replace('ё', '')
s = s.replace('о', '')
s = s.replace('у', '')
s = s.replace('ы', '')
s = s.replace('э', '')
s = s.replace('ю', '')
s = s.replace('я', '')

t = len(s)

print("Cогласные буквы в тексте :" ,t)



