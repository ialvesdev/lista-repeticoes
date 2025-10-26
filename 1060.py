n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
vetNum = [n1, n2, n3, n4, n5, n6]
qtdPositivo = 0
i = 0

while i < len(vetNum):
    if vetNum[i] > 0:
        qtdPositivo+=1
    i+=1
print(f"{qtdPositivo} valores positivos")