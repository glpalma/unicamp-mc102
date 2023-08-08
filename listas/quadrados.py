quadrados = []
cubos = []
n = int(input("Quantos você quer? "))

for i in range(1, n+1):
    quadrado = i ** 2
    quadrados.append(quadrado)
    cubo = i ** 3
    cubos.append(cubo)

print(quadrados)
print(cubos)