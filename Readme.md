Esse projeto foi feito para gerar CPF válidos utilizando o algoritmos do CPF criado pelo Governo Federal. A lógica é bem simples, utilizando Python eu fiz um validador do primeiro digito do CPF após o traço. O algoritmo para isso é bem fácil de entender e eu vou te explicar aqui nesse README.

Para primeiro digito: é necessário pegar cada número do CPF antes do traço e multiplicar cada um dos valores por uma contagem regressiva começando de 10. 
Ex.: 746.824.890-70 (746824890)


   10 9  8  7  6  5  4  3  2 
   7  4  6  8  2  4  8  9  0
= 70 36 48 56 12 20 32 27 0

Somar o resultado das multiplicações e multiplicar novamente por 10.
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11.
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    Resultado é 0.
Contrário disso:
    Resultado é o valor da conta (7).

Então válidando que o primeiro digito, o algoritmo para o segundo é a mesma coisa, mudando apenas o começo da contagem
começa a contar do 11 por causa de ter mais um número descoberto no CPF.


