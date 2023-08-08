saco = float(input("Peso do saco de ração: "))
gato1 = float(input("Quantidade de ração do gato 1 em gramas: "))
gato2 = float(input("Quantidade de ração do gato 2 em gramas: "))

saco = saco * 1000 #transf em gramas

restante = saco - 5 * (gato1 + gato2)
if restante > 0:
    print(f"{restante} gramas")
else:
    print("Os gatos comem demais")