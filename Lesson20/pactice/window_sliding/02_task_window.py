# Дана строка.
# Найти длину самой длинной подстроки без повторяющихся символов.
def all_unique(s: str)-->bool:
   i = 0



a = "мама мыла раму"

left = 0
right = 1
longest_substring = 0

while right < len(a):
    sub_string = a[left:right + 1]
    if not all_same(sub_string):
        if len(sub_string) > longest_substring:
            longest_substring = len(sub_string)
            right = right + 1
            else:
                left = right
                right = left + 1


