n = int(input())
inn = 0
out = 0

for _ in range(n):
    num = int(input())
    if num <= 20 and num >= 10:
        inn += 1
    else:
        out+=1
print(f"{inn} in")
print(f"{out} out")