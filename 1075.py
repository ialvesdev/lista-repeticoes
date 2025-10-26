n = int(input())

for _ in range(n):
    c = int(input())
    if c > 0 and c % 2 == 0:
        print("EVEN POSITIVE")
    elif c > 0 and c % 2 == 1:
        print("ODD POSITIVE")
    elif c == 0:
        print("NULL")
    elif c < 0 and c % 2 == 0:
        print("EVEN NEGATIVE")
    else:
        print("ODD NEGATIVE")