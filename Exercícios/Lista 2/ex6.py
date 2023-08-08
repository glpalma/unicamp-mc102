from math import sqrt

n_str = input()
n_int = int(n_str)

raiz = sqrt(n_int)

numero1 = int(n_str[0] + n_str[1])
numero2 = int(n_str[2] + n_str[3])

if raiz == (numero1 + numero2):
    print("tem")
else:
    print("não tem")