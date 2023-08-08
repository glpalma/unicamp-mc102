def main():
    operacao = input('Digite uma pergunta fundamental: ').split()
    resultado = 0

    while True:
        operador = operacao[1]
        operando1 = int(operacao[0])
        operando2 = int(operacao[2])
        
        if operador == "/":
            resultado = operando1 / operando2
        elif operador == "+":
            resultado = operando1 + operando2
        elif operador == "-":
            resultado = operando1 - operando2
        elif operador == "*":
            resultado = operando1 * operando2
        else:
            print("Caractere de operando inválido.")
        
        if resultado == 42:
            print("Obrigado!")
            break
        else:
            operacao = input('Essa não é uma pergunta fundamental, tente de novo: ').split()

main()