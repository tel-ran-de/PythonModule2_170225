# Задача "Вычисление площади круга"
# Используйте модуль math для получения значения числа π.
# Сгенерируйте случайный радиус круга с помощью модуля random.
# Вычислите площадь круга по формуле πr².
import math
import random
p=math.pi
R= random.randint(1,10)
S= p * (R * 2)

print(S)
