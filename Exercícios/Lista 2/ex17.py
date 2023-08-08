unidade = input()

if unidade == "F":
    print("Digite a temperatura em Fahrenheit:")
    temp_F = float(input())
    temp_C = (5/9)*(temp_F - 32)
    print(temp_C)
elif unidade == "C":
    print("Digite a temperatura em Celsius:")
    temp_C = float(input())
    temp_F = (9/5)*(temp_C) + 32
    print(temp_F)