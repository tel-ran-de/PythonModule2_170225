def is_even(num):
    if  num % 2 == 0 :
        return True
    else:
     return False

n = int(input())
if is_even(n):

 print("Число четное")
else:
 print("Число не четное")
