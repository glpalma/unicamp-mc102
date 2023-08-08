# leia uma sequência de valores de itens e adicione a uma lista 
#

lista_compras = [] #lista vazia

valor = float(input())

while valor >= 0:
    lista_compras.append(valor)
    valor = float(input())
    
print(lista_compras)

# somar todos os valores da lista

soma = 0.0

for valor in lista_compras: #para cada valor na lista de compras 
    soma += valor
print(soma)