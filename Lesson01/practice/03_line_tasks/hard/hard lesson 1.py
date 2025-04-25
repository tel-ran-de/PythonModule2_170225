import math

h, a, b = map(int, input().split())
print(math.sceil((h - b) / (a - b)))
