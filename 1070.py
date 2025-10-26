x = int(input())
i = 1
while i <= 6:
    if x % 2 == 1:
        print(x)
        x += 1
        i+=1
    else:
        x+=1