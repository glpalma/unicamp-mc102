# tive que pedir ajuda #ódio pq não percebi isso antess
x = float(input())

raiz = x ** 0.5

esquerda = (int(raiz/1000)%10) #int retira a parte decimal
direita = (int(raiz*1000)%10) # %10 dá o restin

print(esquerda)
print(direita)