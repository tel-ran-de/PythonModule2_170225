## "Алгоритм Луна"

### Задание

Для шестнадцати значного номера банковской карты, определите корректность ее номера в соответствии с алгоритмом Луна. 

Про Алгоритм Луна можно почитать [тут](https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9B%D1%83%D0%BD%D0%B0) или [тут](https://skobki.com/yazyk-c-proverka-nomera-kreditki/).

### Формат входных данных

Дано целое положительное шестнадцати значное число - номер банковской карты.

### Формат выходных данных

Вывести "Да", если номер карты является корректным или "Нет".

### Решение задачи

```python
## "Алгоритм Луна"
def algorithm_moon(numbers):
    numbers_str = list(str(numbers))
    numbers_list = [int(num) for num in numbers_str[::-1]]
    # print(numbers_list)
    for i in range(1, len(numbers_list), 2):
        numbers_list[i] *= 2
        if numbers_list[i] > 9:
            numbers_list[i] -= 9
    # print(numbers_list)
    # print(sum(numbers_list))
    return True if sum(numbers_list) % 10 == 0 else False

numbers1 = 4026843483168683
numbers2 = 2730168464161841
numbers3 = 5580473372024733
numbers4 = 5580261212024733

print(algorithm_moon(numbers1))
print(algorithm_moon(numbers2))
print(algorithm_moon(numbers3))
print(algorithm_moon(numbers4))
```

---

### Подсказки

<details>
<summary>Подсказка-1</summary>
Для проверки результата можно воспользоваться
<a href="https://ilovecalc.com/calcs/maths/luhn-algorithm/1370/">
этим онлайн калькулятором
</a>
</details>

