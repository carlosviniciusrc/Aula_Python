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

# def saudacao(nome):
#     return f'Seja Bem-Vindo, {nome}'

# pessoa = saudacao('Vinicius')
# print(pessoa)


# def operacao(func, x, y):
#     return func(x,y)

# def soma(a,b):
#     return a + b

# def sub(x,y):
#     return x - y

# calculo = operacao(soma, 5, 5)
# print(calculo)

# def multiplicador(multiplo):
#     def operacao(numero):
#         return numero * multiplo
#     return operacao

# duplicador = multiplicador(2)
# triplicador = multiplicador(3)
# quadruplicador = multiplicador(4)

# print(duplicador(6))
# print(triplicador(2))

# Dicionarios 

# usuario ={
#     'nome': 'Vinicius',
#     'cargo': 'Analista',
#     'idade': 23,
#     'cidade': 'Fortaleza',
#     'estado': 'Ceará'
# }

# usuario['sobrenome'] = 'Rodrigues'
# usuario['nome'] = 'Carlos Vinicius'

# print(usuario['nome'])

# Revisão dia 15/04

# Closure e Higher Order Functions

# def saudacao(nome):
#     return f'Olá, {nome}'

# def operador(func,x,y):
#     return func(x,y)

# def soma(a,b):
#     return a + b

# def subtra(a,b):
#     return a - b

# saudar = saudacao('Vinicius')
# operacao = operador(soma, 1, 2)
# sub = operador(subtra, 100, 10)

# print(saudar)
# print(operacao)
# print(sub)


# def maquina(multiplicador):
#     def resultado(numero):
#         return numero * multiplicador
#     return resultado

# duplicador = maquina(2)
# triplicador = maquina(3)

# print(duplicador(5))
# print(triplicador(2))


# Revisão 17/04

# dicionarios

# mulher = dict(nome='Emilly', idade= 23, cidade= 'Fortaleza')
# mulher['nome'] = 'Emillybtt'


# usuario = {
#     'nome': 'Carlos',
#     'idade': 68,
#     'cidade': 'Fortaleza'
# }

# keys, items, values
# print(tuple(usuario.keys()))
# print(tuple(usuario.values()))
# print(tuple(usuario.items()))

# setdefault
# print(usuario.setdefault('estado','Ceará'))
# print(usuario.setdefault('estado','Ceará'))

# print(usuario)
 
# Revisão 22/04

# dicionarios

# usuario = {
#     'nome': 'Carlos',
#     'idade': 68,
#     'cidade': 'Fortaleza'
# }

# print(len(usuario)) # vai exibir o numero de chaves no dict
# print(usuario.keys()) # Vai exibir as chaves
# print(usuario.values()) # Vai exibir os valores da chaves 
# print(usuario.items()) # Vai exibir o dicionario completo

# v1 = usuario.get('casa', 52) # metodo usado apenas como none para evitar erro no codigo, mas não acrescenta valore no dicionario
# print(v1)

# v2 = usuario.setdefault('estado', 'Ceará') # Diferente do get, ele vai exbir um novo valor e adicionar ao dict

# print(v2)
# print(usuario)

# v3 = usuario.pop('estado') # Vai apagar uma chave dict especifica
# # v4 = usuario.popitem() # Vai deletar o ultimo item do dicionario
# print(usuario)

# Update

# Vai inserir novos dados a chave, caso a chave já exista vai substituir um valor

# lista_nova = {'sobrenome': 'Cardoso', 'bairro': 'Maraponga'}
# usuario.update(lista_nova)
# print(usuario)

# Revisão sobre set()

# lista = ['Vinicius', 1, 2 ,3 ,4]

# conjunto = set(lista)

# conjunto.add('Oi')
# conjunto.clear()

# print(conjunto)

# Revisão dia 14/05

# lista_de_listas_de_inteiros = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
#     [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
#     [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
#     [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
#     [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
#     [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
#     [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
#     [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
#     [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
#     [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
#     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
# ]

# def verificador(lista_de_interios):
#     numeros_checados = set()
#     numero_duplicado = -1

#     for numero in lista_de_interios:
#         if numero in numeros_checados:
#             numero_duplicado = numero
#             break

#         numeros_checados.add(numero)

#     return numero_duplicado


# for lista in lista_de_listas_de_inteiros:
#     print(verificador(lista))

# Revisão Operadores de set - dia 15/05

conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}

# união
conjunto3 = conjunto1 | conjunto2
print(conjunto3)

# Interseção
conjunto4 = conjunto1 & conjunto2
print(conjunto4)

# diferença
conjunto5 = conjunto1 - conjunto2
conjunto6 = conjunto2 - conjunto1
print(conjunto5)
print(conjunto6)

# Diferença simetrica
conjunto7 = conjunto1 ^ conjunto2
print(conjunto7)

