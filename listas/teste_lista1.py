lista = ["Maria", "João", "Raul"]

mesma_lista = lista
outra_lista = []

for nome in lista: #a variavel nome é declarada junto com o for
    outra_lista.append(nome)


lista[2]="Catarina"

print(mesma_lista)
print(outra_lista)
print(nome) #ultimo nome a ser adicionado a outra_lista