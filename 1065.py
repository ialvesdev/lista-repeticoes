x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
i = 0

nums = [x1, x2, x3, x4, x5]
for num in nums:
    if num % 2 == 0:
        i += 1
print(f"{i} valores pares")