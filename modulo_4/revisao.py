# Revisão dia 17/03

# Gerador de CPF

"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# Primeiro Digito
# cpf = '74682489070'
# nove_digitos = cpf[:9]
# contador1 = 10

# resultado1 = 0
# for digito in nove_digitos:
#     resultado1 += int(digito) * contador1
#     contador1 -= 1

# digito1 = (resultado1 * 10) % 11
# digito1 = digito1 if digito1 <= 9 else 0

# # Segundo Digito

# dez_digitos = nove_digitos + str(digito1)
# contador2 = 11

# resultado2 = 0
# for digito in dez_digitos:
#     resultado2 += int(digito) * contador2
#     contador2 -= 1

# digito2 = (resultado2 * 10) % 11
# digito2 = digito2 if digito2 <= 9 else 0

# cpf_complete = nove_digitos + str(digito1) + str(digito2)
# print(cpf_complete)


# Basico de função 

# def novo_mundo():
#     print('Hello World')

# novo_mundo()

# Para chamar uma função utilizamos 'def', após definimos o nome da função 
# e dentro do parenteses passamos o parâmetro e abaixo o bloco de codigo da
# exibição da função

# def soma(x,y):
#     print(f'{x=} {y=} | x + y = ', x + y)
          
# soma(1,2)
# soma(x = -5, y = 2)


# Dia 18/03 - Exercitando um pouco sobre função

# Crie uma função chamada saudacao() que imprime "Olá, bem-vindo!".

# def saudacao():
#     print("Olá, bem-vindo!")

# saudacao()

# Crie uma função chamada cumprimentar(nome), que recebe um nome e imprime "Olá, [nome]!".

# def cumprimentar(nome):
#     print(f'Olá, {nome}!')

# cumprimentar('Vinicius')

# Crie uma função chamada dobro(numero), que recebe um número e retorna seu dobro.

# def dobro(numero):
#     print(f'Seu numero dobrado é {numero} =', numero * 2)

# dobro(2)

# Escreva uma função chamada soma(a, b) que recebe dois números e retorna a soma deles.

# def soma(a, b):
#     print(f'A soma de {a} + {b} =', a + b)

# soma(2, 2)

# Crie uma função chamada eh_par(numero), que retorna True se o número for par e False se for ímpar.

# def eh_par(numero):
#     if numero % 2 == 0:
#         print(numero % 2 == 0)
#     else:
#         print(numero % 2 == 0)

# eh_par(2)

# Crie uma função chamada contagem_regressiva(n), que imprime os números de n até 0 usando recursão.

# Dia 20/03

#fixação de 'return'

# def saudacao():
#     return "Olá, seja bem-vindo"

# mensagem = saudacao()
# print(mensagem)

# Crie uma função chamada media(nota1, nota2, nota3), 
# que calcula e retorna a média aritmética de três notas.

# def media(nota1, nota2, nota3):
#     media_calculada = float((nota1 + nota2 + nota3) / 3)
#     return media_calculada 


# media_augusto = media(7,5,9)

# print(media_augusto)

# media_vini = media(10, 9, 5)

# print(media_vini)

# numeros = 1, 2, 3, 4, 5, 6
# print(sum(numeros))]

# Dia 01/04 - pratica sobre funçoes de primeria classe

# def saudacao():
#     return 'Olá mundo'

# ola = saudacao

# print(ola())

# def operador(x, y, funcao):
#     return funcao(x, y)

# def soma(a, b):
#     return a + b

# def multiplica(a, b):
#     return a * b

# somador = operador(1, 2, soma)

# print(somador)

# Dia 02/04 - revisão sobre Higher Order Functions

# def menu(func, x, y):
#     return func(x,y)

# def soma(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def divi(a, b):
#     return a // b

# def multi(a,b):
#     return a * b

# operacao = menu(multi, 2, 1)
# print(operacao)

# Dia 04/04 - revisão sobre closure 

# def saudacao(frase):
#     def pessoa(nome):
#         return f'{frase}, {nome}'
#     return pessoa

# apresentacao = saudacao('Seja Bem-vindo')
# print(apresentacao('Vinicius'))


# def operador(multiplicador):
#     def operacao(numero):
#         return numero * multiplicador
#     return operacao

# duplicador = operador(2)
# triplicador = operador(3)
# quadruplicador = operador(4)

# print(duplicador(20))

# Dia 07/04 - revisão

# Closeure e Higher Order Functions

def saudacao(nome):
    return f'Seja Bem-Vindo, {nome}'

pessoa = saudacao('Vinicius')
print(pessoa)


def operacao(func, x, y):
    return func(x,y)

def soma(a,b):
    return a + b

def sub(x,y):
    return x - y

calculo = operacao(soma, 5, 5)
print(calculo)

def multiplicador(multiplo):
    def operacao(numero):
        return numero * multiplo
    return operacao

duplicador = multiplicador(2)
triplicador = multiplicador(3)
quadruplicador = multiplicador(4)

print(duplicador(6))
print(triplicador(2))

# Dicionarios 

usuario ={
    'nome': 'Vinicius',
    'cargo': 'Analista',
    'idade': 23,
    'cidade': 'Fortaleza',
    'estado': 'Ceará'
}

usuario['sobrenome'] = 'Rodrigues'
usuario['nome'] = 'Carlos Vinicius'

print(usuario['nome'])

