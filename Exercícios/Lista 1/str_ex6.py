texto = input()
texto = texto + "1" # FIXME: se a string terminar em 0, dá problema de índice
n_zeros = 0 # corrigido adicionando um "1" no final da string digitada
lista_zeros = []

for i in range(len(texto)):
    if texto[i] == "0":
        n_zeros += 1
        if texto[i + 1] == "1":
            lista_zeros.append(n_zeros)
            n_zeros = 0

maior = 0
for j in range(len(lista_zeros)):
    if lista_zeros[j] > lista_zeros[j-1]:
        maior = lista_zeros[j]

print(maior)