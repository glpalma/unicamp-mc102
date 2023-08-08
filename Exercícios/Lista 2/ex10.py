from math import sqrt

def ler_coeficientes():
    A = float(input())
    B = float(input())
    C = float(input())
    return A, B, C

def calcular_delta(A, B, C):
    delta = ((B**2) - 4*A*C)
    print(delta)
    return delta

def calcular_raizes(A, B, delta):
    if delta < 0:
        print("RAÍZES IMAGINÁRIAS")
    elif delta == 0:
        print("RAÍZ ÚNICA")
        raiz = (-B)/(2*A)
        print(f"Raiz: {raiz}")
    elif delta > 0:
        print("RAÍZES DISTINTAS")
        raiz1 = ((-B) + sqrt(delta))/(2*A)
        raiz2 = ((-B) - sqrt(delta))/(2*A)
        print(f"As raízes são: {raiz1} e {raiz2}")

def main():
    A, B, C = ler_coeficientes()
    delta = calcular_delta(A, B, C)
    calcular_raizes(A, B, delta)

main()