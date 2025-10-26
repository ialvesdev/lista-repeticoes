x = int(input())
y = 1

while y != x:
    if y % 2 == 1:
        print(y)
    y+=1
    
if y == x and y % 2 == 1:
    print(y)
    