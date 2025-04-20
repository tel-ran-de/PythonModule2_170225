## "Совершенное число"

### Задание

Число совершенно, если оно равно сумме всех своих делителей, кроме самого себя. Пример: 6 = 1 + 2 + 3. \
Проверить, является ли данное число совершенным.

### Формат входных данных

Дано целое положительно число.

### Формат выходных данных

Вывести "Да", если число совершенно и "Нет" в противоположном случае.

### Решение задачи

```python
def is_ideal_number(n: int) -> bool:
    num_sum = [ i  for i in range(1, n + 1) if not i == n and n % i == 0]
    return sum(num_sum) == n
    # if sum(num_sum) == n:
    #     return True
    # return False

assert is_ideal_number(4) == False     # Нет
assert is_ideal_number(6) == True      # Да
assert is_ideal_number(14) == False    # Нет
assert is_ideal_number(22) == False    # Нет
assert is_ideal_number(28) == True     # Да
assert is_ideal_number(100) == False   # Нет
assert is_ideal_number(496) == True    # Да
```

---

### Данные для самопроверки

| Дано | Результат |
| :---: | --- |
|    4    | Нет |
|    6    | Да  |
|    14    | Нет |
|    22    | Нет |
|    28    | Да  |
|    100    | Нет  |
|    496   | Да  |
### Подсказки

<details>
<summary>Подсказка-1</summary>
Воспользуйтесь решение предыдущей задачи "Делители числа" и найдите их сумму.
</details>
