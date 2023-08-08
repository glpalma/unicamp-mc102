entrada = input()

aux = ''

n = len(entrada)
for i in range(n):
    if entrada[i] != ' ':
        aux += entrada[i]

m = len(aux)

for j in range(m):
    eh_palindromo = True
    if aux[j] != aux[m-j-1]:
        eh_palindromo = False
        break

if eh_palindromo:
    print("Palíndromo")
elif not eh_palindromo:
    print("Não Palíndromo")