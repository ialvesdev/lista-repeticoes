i = 0
valores = []
pos_maior = 0

while i < 100:
    num = int(input())
    valores.append(num)
    i += 1

maior = valores[0]
j = 1
while j < len(valores):
    if valores[j] > maior:
        maior = valores[j]
        pos_maior = j + 1
    j += 1

print(maior)
print(pos_maior)