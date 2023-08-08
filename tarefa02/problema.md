# Problema

O problema a seguir consiste no desenvolvimento de um algoritmo que possibilite a adição de um determinado número de dias a uma data específica. Com o arquivo __algoritmo1.md__, o usuário fornecerá uma data e o número a ser somado a ela como entrada. Como saída, o algoritmo devolverá uma nova data, correspondente à soma do número à data fornecida.\
Se a soma do número fornecido com o dia da data for maior que o total de dias no mês em questão, a contagem será reiniciada no mês seguinte.

## Entrada
-  Números positivos inteiros, onde `dd` é o dia, `mm` é o mês, `aa` é o ano e `xx` é o número a ser adicionado.

## Saída
- Uma data no formato `dd/mm/aa`. 
## Exemplos
1. Se o usuário fornecer a data 24/03/20 e o número 4, a data de saída será o dia 28/03/20.
2. Se a entrada for a data 24/03/20 e o número 15, o algoritmo contará 7 "passos" até o dia 31/03 e continuará a partir do dia 01/04 até chegar ao dia 08/04.
3. Se o número fornecido for 365 (número de dias em um ano), a saída será igual à data de entrada.