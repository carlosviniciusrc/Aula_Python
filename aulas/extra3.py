# Exercícios com while

# Imprimir os números de 1 a 10.

# i = 0

# while i <= 10:
#     print(i)

#     i += 1

# Pedir ao usuário para digitar números até ele digitar 0.


# while True:
#     try:
#         numero = int(input('Digite um número: '))

#         if numero == 0:
#             print('Você chegou no numero correto! Parabéns!')
#             break
#         else:
#             print('Digite outro número')
#             continue
#     except:
#         print('Digite apenas numeros')
#         continue

# Validar uma senha que o usuário deve digitar até acertar

# while True:
#     try:
#         nome = input('Digite seu nome: ')
#         senha = input('Digite sua senha: ')
#         senha_correta = '1234'

#         if senha == senha_correta:
#             print('Acesso liberado', end= '\n')
#             print(f'Seja Bem-Vindo {nome}')
#             break
#         else:
#             print('Senha incorreta, digite novamente sua senha')
#             continue
#     except:
#         print('Digite apenas numeros')
#         continue

# Calcular a soma de números digitados pelo usuário até que ele digite um número negativo.

# soma = 0

# while True:
#     numero1 = int(input('Digite um número para realizar a soma: '))
#     numero2 = int(input('Digite outro número para realizar a soma: '))

#     if (numero1 < 0) or (numero2 < 0):
#         break
    
#     soma = numero1 + numero2

#     print(F'O resultado da soma dos números é {soma}')


# soma = 0  # Inicializa a soma em 0

# while True:
#     numero = int(input("Digite um número (negativo para sair): "))
#     if numero < 0:
#         break  # Encerra o loop se o número for negativo
#     soma += numero  # Adiciona o número à soma

# print(f"A soma dos números digitados é: {soma}")

# Contar de 1 a 100, mas parar se encontrar o número 42 (use uma condição dentro do loop).

# i = 0

# while i <= 100:
#     print(i)
#     i += 1

#     if i == 42:
#         break

# teste aleatorio

# qtd_linhas = 5
# qtd_colunas = 5

# linha = 1

# while linha < qtd_linhas:
#     coluna = 1
#     while coluna <= qtd_colunas:
#         print(f'{linha=},{coluna=}')
#         coluna += 1
#     linha +=1

# Pedir ao usuário para digitar uma palavra e parar quando a palavra digitada for "sair".

# while True:
#     palavra = input('Digite uma palavra (sair para finalizar): ').lower()

#     if palavra == 'sair':
#         print('Finalizado')
#         break

#     print(palavra)

# Imprimir a sequência de Fibonacci até que o valor ultrapasse 100.

# a, b = 0, 1

# while a <= 100:
#     print(a)
#     a, b = b, a + b

# Exercícios com for:

# Imprimir os números de 1 a 10.

# for i in range(11):
#     print(i)

# Imprimir os números ímpares de 1 a 20.

# for i in range(1,21):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)

# Calcular a soma de todos os números de 1 a 50.
# soma = 0
# for i in range(1,51):
#     soma += i

# print(soma)

# Imprimir a tabuada de um número fornecido pelo usuário.

# numero = int(input('Digite um número para saber a tabuada: '))

# for i in range(11):
#     valor = numero * i
#     print(f'{numero} x {i} = {valor}')

# Percorrer uma lista de nomes e imprimir cada nome.

# lista = ['maça', 'uva', 'banana']

# for i in lista:
#     print(i)

# Imprimir os números de 10 a 1 em ordem decrescente.

# for i in range(10, -1, -1):
#     print(i)

# Contar quantos números pares existem em uma lista

# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# contador = 0

# for i in lista:
#     if i % 2 == 0:
#         contador += 1

# print(f"Quantidade de números pares: {contador}")


# relembrando 

# import os

# palavra_secreta = 'vini'
# letras_acertadas = ''
# numero_tentativas = 0

# while True:
#     letra_digitada = input('Digite uma letra: ')

#     numero_tentativas += 1

#     if len(letra_digitada) > 1:
#         print('Digite apenas uma letra')
#         continue

#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada

#     palavra_formada = ''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += '*'

#     print(palavra_formada)

# relembrando  2

# notas = [7.5, 9.0, 6.7, 2.2, 4.3, 7.8, 10.00, 9.7]

# soma_notas = 0
# nota_mais_alta = notas[0]
# nota_mais_baixa = notas[0]

# for nota in notas:
#     soma_notas += nota

#     if nota > nota_mais_alta:
#         nota_mais_alta = nota
#     if nota < nota_mais_baixa:
#         nota_mais_baixa = nota

# media_nota = soma_notas / len(notas)

# acima_da_media = 0

# for nota in notas:
#     if nota > media_nota:
#         acima_da_media += 1

# print(nota_mais_alta)
# print(nota_mais_baixa)
# print(media_nota)
# print(acima_da_media)

# enumerate 

# lista = ['Carlos', 'Rafaella', 'Vinicius']

# print(enumerate(lista))

# for numero, nome in enumerate(lista):
#     print(numero, nome)

# print(numero, nome)

import random

print(random.randint(0,9))

