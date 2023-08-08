string = list(input())
termo = input()
# print(string)
string_nova = []
texto_novo = "" # string vazia

for i in range(len(string)):
    string_nova.append(string[i])
    if termo == string[i+1]: # se for string[i], o termo é considerado
        break
    # print(string_nova)

for j in range(len(string_nova)):
    texto_novo = texto_novo + string_nova[j]
    # print(texto_novo)

print(texto_novo)