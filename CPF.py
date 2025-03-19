import random

cpf = ''
for i in range(9):
    cpf += str(random.randint(0, 9))

print(f'CPF Base: {cpf}')
#verifica o primeiro digito
nove_digitos = cpf
contador = 10
soma = 0
for digito in nove_digitos:
    soma += int(digito) * contador
    contador -= 1

resultado = (soma * 10) % 11
resultado = 0 if resultado >= 10 else resultado

print(f'O primeiro dígito do CPF é {resultado}')

#verifica o segundo dígito
dez_digitos = cpf + str(resultado)
contador2 = 11
soma2 = 0
for digito2 in dez_digitos:
    soma2 += int(digito2) * contador2
    contador2 -= 1

resultado2 = (soma2 * 10) % 11
resultado2 = 0 if resultado2 >= 10 else resultado2

print(f'O segundo dígito do CPF é {resultado2}')

#cpf final
cpf_final = f'{cpf}{resultado}{resultado2}'
cpf_formatado = f'{cpf_final[:3]}.{cpf_final[3:6]}.{cpf_final[6:9]}-{cpf_final[9:]}'

print(f'CPF Final: {cpf_formatado}')






