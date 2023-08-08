# lê uma string com três partes
a, b, c = input().split()

# converte strings em números
a = float(a)
b = float(b)
c = float(c)

# termine esse programa aqui...

condicao_existencia = a < (b + c) and b < (a + c) and c < (a + b)

if a >= b and a >= c: # Determinação do maior lado
    hipotenusa = a
    cateto1 = b
    cateto2 = c
elif b >= a and b >= c:
    hipotenusa = b
    cateto1 = a
    cateto2 = c
elif c >= a and c >= b:
    hipotenusa = c
    cateto1 = a
    cateto2 = b

cosseno = ((cateto1**2) + (cateto2**2) - (hipotenusa ** 2))/(2*cateto1*cateto2)
# lei dos cossenos

if condicao_existencia:
    if cosseno == 0:
        print("retângulo")
    if cosseno > 0:
        print("acutângulo")
    if cosseno < 0:
        print("obtusângulo")
else:
    print("não forma triângulo")