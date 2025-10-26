x = int(input())
y = int(input())
total = 0
if x < y:
    for num in range((x + 1), y):
        if num % 2 == 1:
            total += num
else:
    for num in range((y + 1), x):
        if num % 2 == 1:
            total += num
    
    
print(total)
