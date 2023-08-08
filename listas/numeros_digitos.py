n = int(input())

digitos = 0

while n > 0:
    n = n // 10 #retira o último dígito ex: 12//10 == 1 (seria 1.2, mas só a parte do 1 é considerada)
    digitos += 1

print(f"O número dde dígitos é {digitos}")