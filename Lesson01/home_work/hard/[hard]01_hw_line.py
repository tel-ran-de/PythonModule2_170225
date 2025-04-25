seconds = int(input())

days = seconds // 86400
seconds %= 86400

hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

print(days, "дней", hours, "часов", minutes, "минут", seconds, "секунд")
