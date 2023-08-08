"""
É possível trocar o valor de duas variáveis sem usar uma outra 
variável adicional, mas só em Python, cujas variáveis possuem
tamanho varíavel. Em outras línguas, como o C, essa operação pode
causar overflow.
"""

x = int(input())
y = int(input())

y = y + x
x = y - x
y = y - x

print(x)
print(y)