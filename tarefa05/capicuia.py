#-*- codification:utf-8 -*- 
"""
CAPICUIA

capicuia int((input)) --> número a ser checado. deve ser inteiro e positivo 
    - deve ser lido como int
    - convertido para string (para poder usar a função len)

if len ==  4
    if  o (último e o primeiro) e o (penúltimo e o segundo são iguais):
        printar sim
    else:
        não

if len == 3 or len == 2: #dois e três têm a mesma condição, logo é melhor uní-los com um "ou"
    if último e primeiro são iguais:
        print sim
    else: 
        print não

                                        if len == 2: 
                                            if ultimo e penultimo sao iguais
                                                print sim
                                            else:
                                                print não

if len == 1:
    print sim

"""
capicuia = input() #input já lê como string
comprimento = len(capicuia)

if comprimento == 4:
    if (capicuia[0] == capicuia[-1]) and (capicuia[1] == capicuia[-2]):
        print("sim")
    else:
        print("não")
    
if comprimento == 3 or comprimento == 2:
    if capicuia[0] == capicuia[-1]:
        print("sim")
    else:
        print("não")

if comprimento == 1:
    print("sim")