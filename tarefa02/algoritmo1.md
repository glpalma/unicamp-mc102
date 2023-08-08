# Algoritmo 1 
## Adição de um número a uma data, ambos fornecidos como entrada, resultando em uma nova data.
O algoritmo aceitará como entrada um número no formato `xx` e uma data no formato `dd/mm/aa`, como por exemplo 15 e 24/03/20.

Para executá-lo, os seguintes passos devem ser seguidos:
1. Primeiramente, receba a entrada `xx` e o dia `dd/mm/aa`;
2. Verifique se `xx` > 365;\
__2.2.__ Se sim, pule um ano e comece a contagem com `xx - 365`; \
    2.2.1. Se o número resultante for maior do que o número de dias necessário para que o mês fornecido na data acabe;\
    2.2.2. Conte até o último dia do mês fornecido (`mm`);\
    2.2.3. Continue a contagem no mês seguinte a partir do primeiro dia, utilizando o número que restou do tópico 2.2.2;\
    2.2.4. Forneça como saída a data do mês seguinte no formato `dd/mm/aa`.\
__2.3.__ Se não, verifique se o número for maior do que o número de dias necessário para que o mês fornecido na data acabe;\
    2.3.1. Se for maior, conte até o último dia do mês fornecido (`mm`);\
    2.3.2. Continue a contagem no mês seguinte a partir do primeiro dia, utilizando o número que restou do tópico 2.2.2;\
    2.3.3. Forneça como saída a data do mês seguinte no formato `dd/mm/aa`.\
    2.3.4. Se for menor, some o número `xx` ao número do dia e exiba a nova data como saída. 
