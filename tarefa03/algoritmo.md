# Algoritmo
## Apontamento do número com o maior número de divisores dentre números de uma lista fornecida como entrada 

__Instruções:__
1. Receba como entrada uma lista de ``n`` números inteiros positivos;
2. Aponte para o primeiro número da lista;
3. Anote uma variável ``di = 0``, onde i é o número do índice do número apontado na lista. ``di`` guardará o número de vezes que a divisão resultou em um número inteiro;
4. Divida o número apontado por todos os números entre 1 e ele mesmo;
5. Para cada divisão que resulte em um número inteiro, some 1 a ``di``;
6. Aponte para o próximo item da lista;
7. Se i for menor ou igual a n, repita o ciclo;
8. Compare os valores de ``di`` anotados para os diversos números da lista;
9. Forneça como saída o número representado pelo índice do maior valor entre os ``di`` presentes.
