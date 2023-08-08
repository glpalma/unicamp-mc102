"""
Algoritmo:

1) leia um número n
2) lista <-- leia n números de ponto flutuante
3) notas_maiores <-- cópia das notas maiores que 5 de lista
4) calcular a média dos valores em notas_maiores

"""
n = int(input())
lista = []
i = 0 #número de vezes que li um número do teclado 

while i < n:
    numero = float(input())
    i += 1
    lista.append(numero)

notas_maiores = []

for nota in lista:
    if nota >= 5:
        notas_maiores.append(nota)

soma = 0
for nota in notas_maiores:
    soma += nota

media = float(soma/len( notas_maiores))

print(f"{media:.1f}") #ou print("{:.1}".format(media))