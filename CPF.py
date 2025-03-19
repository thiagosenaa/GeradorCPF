
cpf = input('Escreva o CPF: ')
nove_digitos = cpf.replace('.', '').replace('-', '')
nove_digitos = nove_digitos[:-2]

contador = 11
soma = 0
for digito in nove_digitos:
   contador -= 1
   soma += int(digito) * contador

resultado = soma % 11

if resultado <  2:
    resultado = 0
elif resultado >= 2:
    resultado = 11 - resultado

print(f'O primeiro digito do CPF é {resultado}')

dez_digitos = cpf.replace('.', '').replace('-', '')
dez_digitos = dez_digitos[:-1]

contador2 = 12
soma2 = 0
for digito2 in dez_digitos:
    contador2 -= 1
    soma2 += int(digito2) * contador2

resultado2 = soma2 % 11

if resultado2 <  2:
    resultado2 = 0
elif resultado2 >= 2:
    resultado2 = 11 - resultado2

print(f'O segundo digito do CPF é {resultado2}')







