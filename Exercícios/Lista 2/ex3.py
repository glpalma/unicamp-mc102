numeros = input().split()

maior = numeros[0]
for valor in numeros:
    if valor > maior:
        maior = valor

print(maior)