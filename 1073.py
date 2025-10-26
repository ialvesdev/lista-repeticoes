import math
n = int(input())
y = 0


for num in range(1, (n+1)):
    if num % 2 == 0:
        y = math.pow(num, 2)
        y = int(y)
        print(f"{num}^2 = {y}")