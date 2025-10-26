x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
pares = 0
impares = 0
positivos = 0
negativos = 0

nums = [x1, x2, x3, x4, x5]
for num in nums:
    if num % 2 == 0:
        pares += 1
    if num % 2 == 1:
        impares += 1
    if num > 0:
        positivos += 1
    if num < 0:
        negativos += 1
    
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")