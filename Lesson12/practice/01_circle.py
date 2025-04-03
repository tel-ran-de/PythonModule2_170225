# Задача "Вычисление площади круга"
# Используйте модуль math для получения значения числа π.
# Сгенерируйте случайный радиус круга с помощью модуля random.
# Вычислите площадь круга по формуле πr².
<<<<<<< HEAD
import math
import random

r = random.randint(1, 20)
r = math.pi * r ** 2
print(r)
=======

import math
from random import randint

r = randint(1, 20)
area = math.pi * r * r
print(area)
>>>>>>> 4f7cf1bf3d2dc2459cdaff08dc9316c53615f96f
