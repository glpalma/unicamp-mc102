# Receba uma sequência de nomes digitados e imprima as iniciais
# Para sinalizar que não há mais nomes, o usuário irá digitar um traço

#Entrada: Maria João Pedro Catarina -
#Saída: M J P C 

lista_nomes = []
nome = input()

while nome != "-":
    lista_nomes.append(nome)
    nome = input()

# guardar as iniciais 

lista_iniciais = []
for nome in lista_nomes:
    inicial = nome[0]
    if inicial not in lista_iniciais: #para evitar que a mesma letra apareça duas vezes
        lista_iniciais.append(inicial)

print(lista_iniciais)