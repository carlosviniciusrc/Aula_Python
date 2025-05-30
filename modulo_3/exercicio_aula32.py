"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um numero inteiro: ')

try:
    numero_inteiro = int(numero) #poderia tambem ter usado .isdigit()

    if numero_inteiro % 2 == 0:
        print('O número que você digitou é par')
    else:
        print('O número que você digitou é ímpar')

except:
    print('Você não digitou um número inteiro')

# metodo 2

if numero.isdigit():
    numero_convertido = int(numero)
    numero_par_impar = numero_convertido % 2 == 0
    par_impar_texto = 'ímpar'

if numero_par_impar:
    par_impar_texto = 'par'

    print(f'O número {numero_convertido} é {par_impar_texto}')
else:
    print(f'Você não digitou um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

numero = input('Digite a hora em números inteiros:')

try:
    hora = int(numero)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Hora invalida')
except:
    print('Você não digitou um número inteiro')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome:')
num_nome = len(nome)

if num_nome <= 4:
    print('Seu nome é curto')
elif num_nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')