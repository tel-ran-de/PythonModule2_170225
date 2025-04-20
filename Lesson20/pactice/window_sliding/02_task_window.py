# Дана строка.
# Найти длину самой длинной подстроки без повторяющихся символов.
<<<<<<< HEAD
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


=======

def all_unique(s: str) -> bool:
    return len(s) == len(set(s))


#         l  r
string = "hello world"
left = 0
right = 1
longest_sub_string = 0

while right < len(string):
    sub_string = string[left:right + 1]
    if all_unique(sub_string):
        if len(sub_string) > longest_sub_string:
            longest_sub_string = len(sub_string)
        right += 1
    else:
        left = right
        right = left + 1

print(longest_sub_string)
>>>>>>> abc6f5ff0e2b20d44f736240634f8321d0bfa1a5
