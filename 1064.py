n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

vetNum = [n1, n2, n3, n4, n5, n6]

qtdPositivo = 0
vetPos = []
i = 0

while i < len(vetNum):
    if vetNum[i] > 0:
        qtdPositivo += 1
        vetPos.append(vetNum[i])
    i += 1

total = 0
for pos in vetPos:
    total += pos

media = total / qtdPositivo

# Mostrar resultado
print(f"{qtdPositivo} valores positivos")
print(f"{media:.1f}")