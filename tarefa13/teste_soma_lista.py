from jobs import soma_pesos, menor_valor

def main():
    lista = [3, 5, 6, 0, 10, 10] # soma = 32
    soma = soma_pesos(lista)
    valor = menor_valor(lista)
    print(soma)
    print(valor)

main()