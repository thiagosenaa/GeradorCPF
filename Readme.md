Esse projeto foi feito para gerar CPF válidos utilizando o algoritmos do CPF criado pelo Governo Federal. A lógica é bem simples, utilizando Python eu fiz um validador do primeiro digito do CPF após o traço. O algoritmo para isso é bem fácil de entender e eu vou te explicar aqui nesse README.

Para primeiro digito: é necessário pegar cada número do CPF antes do traço e multiplicar cada um dos valores por uma contagem regressiva começando de 10. 
Somar o resultado das multiplicações e multiplicar novamente por 10.
Obter o resto da divisão da conta anterior por 11.
Se o resultado anterior for maior que 9:
    Resultado é 0.
Contrário disso:
    Resultado é o valor da conta (7).

Então válidando que o primeiro digito, o algoritmo para o segundo é a mesma coisa, mudando apenas o começo da contagem
começa a contar do 11 por causa de ter mais um número descoberto no CPF.


