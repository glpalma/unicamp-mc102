# -*- coding:utf-8 -*-

print("Para fazer uma soma de P.A., digite os numeros pedidos.")

a1 = int(input("Digite o primeiro termo da P.A.: "))
razao = int(input("Digite a razão: "))
an = int(input("Digite o n-esimo termo: "))
soma = 0

while a1 <= an:
    soma += a1
    a1 += razao
print("A soma da P.A. e {}".format(soma))