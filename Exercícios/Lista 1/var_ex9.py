# Cálculo do determinante de uma matriz 2x2

print("""Digite a matriz com os seguintes termos:
|a b|
|c d|
""")

a, b, c, d = input().split()
a = float(a)
b = float(b)
c = float(c)
d = float(d)

det = (a*d) - (b*c)
print(det)