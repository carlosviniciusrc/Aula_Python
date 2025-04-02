# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multi(*args):
    multiplicador = 1
    for numero in args:
        multiplicador *= numero
    return multiplicador

teste1 = multi(1, 2, 3, 4, 5)
print(teste1)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def tipo(numero):
    if numero % 2 == 0:
        return 'Seu numero é par'
    else:
        return 'Seu numero é ímpar'

resultado = tipo(5)
print(resultado)

# Modo 2:

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    
    return f'{numero} é impar'

print(par_impar(5))
print(par_impar(2))
