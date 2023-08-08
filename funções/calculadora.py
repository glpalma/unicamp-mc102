import math

def operacao_soma():
    n1 = float(input())
    n2 = float(input())
    soma = n1 + n2
    print(soma)

def operacao_subtracao():
    n1 = float(input())
    n2 = float(input())
    diferenca = n1 - n2
    print(diferenca)

def operacao_multiplicacao():
    n1 = float(input())
    n2 = float(input())
    produto = n1 * n2
    print(produto)

def operacao_divisao():
    n1 = float(input())
    n2 = float(input())
    if n2 == 0:
        print("Divisor não pode ser 0")
        return #em vez do continue, deve-se usar o 
        # return, que faz o código voltar para onde (foi chamado)
    produto = n1 / n2
    print(produto)

def operacao_raiz():
    num = float(input())
    if num < 0:
        print("Não existe raiz quadrada de números negativos.")
        return # mesma coisa que na divisão 
    raiz = math.sqrt(num)
    print(raiz)

def minha_sqrt(radiando):
    pass #TODO: método de Newton a ser implementado 

while True:
    operacao = input()
    if operacao == "+":
        operacao_soma()
    elif operacao == "-":
        operacao_subtracao()
    elif operacao == "*":
        operacao_multiplicacao()
    elif operacao == "/":
        operacao_divisao()
    elif operacao == "sqrt":
        operacao_raiz()
    elif operacao == "F":
        break
    else:
        print("Operação inválida.")