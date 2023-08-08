# Agenda.py

O __agenda.py__ é um programa escrito em Python cujo funcionamento se baseia em torno da linha de comando. Todas as interações com ela são feitas por meio de argumentos, que definem a ação a ser executada. 

Para executar qualquer ação sobre a agenda, é necessário digitar `-a` após `agenda.py` ser invocado.

Na linha de comando, cada dado sobre o evento deve ser escrito após se indicar sua categoria. Para indicar o nome do evento, deve-se escrever `--nome`, seguido do nome do evento. O mesmo vale para a `--data`, `--descricao`, `evento` e `--hora`.

## 1. Ações básicas
Primeiramente, é necessário criar uma agenda antes de executar quaisquer alterações com o seguinte comando:

`python3 agenda.py -a suaagendaaqui.csv inicializar` 

Após o arquivo da agenda ser criado, o usuário poderá listar os eventos de um dia, criar, alterar e remover eventos. Se não houver eventos para tal dia, o usuário será notificado.

Exemplo de criação de um evento: 

`python3 agenda.py -a suaagendaaqui.csv criar
--nome NOME --data DATA --descricao DESCRICAO --hora HORA`

Exemplo de alteração de um horário:

`python3 agenda.py -a suaagendaaqui.csv alterar --evento ÍNDICE --hora HORA` 

Exemplo de remoção de um evento:

`python3 agenda.py -a suaagendaaqui.csv remover --evento ÍNDICE` 

Exemplo de listagem dos eventos de um dia: 

`python3 agenda.py -a suaagendaaqui.csv listar --data DATA`

## 2. Armazenamento dos dados

O armazenamento dos dados da agenda é feito em um arquivo de texto do formato CSV, cujo nome é fornecido pelo usuário na hora de inicializar e modificar a agenda.

A estrutura do arquivo é simples, isto é, é constituído apenas das informações sobre os eventos. Cada coluna representa uma classe de informações sobre os eventos: é na primeira coluna que estão situados os índices dos eventos; na segunda ficam os nomes; na terceira, as descrições; na quarta, as datas e na quinta, os horários.

`identificador,nome,descrição,data,hora`

Cada linha do arquivo representa um evento. Nela, as informações sobre o evento estão separadas por vírgulas e da forma mostrada.

"identificador" representa o índice do evento na agenda e é definido pela ordem de criação do evento. Nesse sentido, se a agenda estiver vazia, o primeiro evento terá identificador igual a 1; se já tiver 10 eventos, um evento novo terá identificador 11. 

## 3. Estrutura de dados
 
Para que essas informações sejam manipuladas pelo programa, elas devem ser adaptadas à linguagem em que este foi escrito: Python. 
Nesse viés, a agenda possui uma estrutura definida dentro do programa que possibilita tais modificações. No __agenda.py__, a agenda é representada por uma lista de dicionários, em que cada dicionário representa um evento.

Como cada evento é representado por um `dict()`, as informações são organizadas em `chave:valor`.
As chaves são iguais às colunas. Logo, ao selecionar um item da agenda e fornecer a ele uma chave (Ex: `evento['data']`), a estrutura devolve a informação correspondente. Isso facilita a manipulação das informações e o entendimento do código, pois explicita as informações sendo manipuladas. 