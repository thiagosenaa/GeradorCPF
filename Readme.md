Esse projeto foi feito para gerar CPF válidos utilizando o algoritmos do CPF criado pelo Governo Federal. A lógica é bem simples, utilizando Python eu fiz um validador do primeiro digito do CPF após o traço. O algoritmo para isso é bem fácil de entender e eu vou te explicar aqui nesse README.

Para primeiro dígito: é necessário pegar cada número do CPF antes do traço e multiplicar cada um dos valores por uma contagem regressiva começando de 10, após a multiplicação, some o resultado e multiplicar novamente por 10, depois o resto da divisão da conta anterior por 11.

Se o resultado anterior for maior que 9:
    Resultado é 0.
Contrário disso:
    Resultado é o primeiro dígito da conta.

Então válidando que o primeiro digito, o algoritmo para o segundo é a mesma coisa, mudando apenas o começo da contagem começa a contar do 11 por causa de ter mais um número descoberto no CPF.


