# Exercícios Básicos

# Imprima os números de 1 a 10: Crie um programa que utilize um laço for para imprimir os números de 1 a 10.

# for i in range(1,11):
#     print(i)

# Imprima os números pares de 1 a 20: Escreva um programa que exiba apenas os números pares entre 1 e 20.

# for numero in range(0,21):
#     if numero % 2 == 0:
#         print(numero)

"""
Explicação do Código:
-range(1, 21):

O range gera números de 1 a 20 (o último número do range é exclusivo, então usamos 21 para incluir o 20).

-Condição if numero % 2 == 0:

O operador % (módulo) calcula o resto da divisão do número por 2.
Se o resto for igual a 0, significa que o número é par.

-print(numero):

Imprime apenas os números que passaram na condição.
"""

# Soma de números de 1 a N: Solicite ao usuário um número N e calcule a soma de todos os números de 1 a N.

# n = int(input('Digite um numero: '))

# soma = 0

# for i in range(1, n + 1):
#     soma += i
# print(soma)


# Exercícios Intermediários

# Tabuada: Peça ao usuário um número e exiba a tabuada desse número de 1 a 10.

# numero = int(input('Digite um numero: '))

# soma_produto = 0

# for i in range(1,11):
#     produto = numero * i
#     soma_produto += produto
#     print(f'{numero} x {i} = {produto}')

# print('A soma de todos os produto é', soma_produto)

# Fatorial: Solicite ao usuário um número N e calcule o fatorial de N utilizando um laço for.

# n = int(input('Digite um numero: '))

# fatorial = 1

# for numero in range(1, n + 1):
#     fatorial *= numero

# print(fatorial)

# Contagem regressiva: Crie um programa que exiba uma contagem regressiva 
# de 10 até 0 e, ao final, exiba a mensagem "Feliz Ano Novo!".

# for numero in range(10, 0, -1):
#     print(numero)

# print('Feliz Ano Novo!')

# Números divisíveis por 3 e 5: Mostre todos os números entre 1 e 100 que são divisíveis por 3 e por 5.

# for i in range(1, 100):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)


# nomes = ["Ana", "Bruno", "Carlos", "Pedro", "João"]

# entrada = input('jsjsjks: ')

# nomes.remove(entrada) # Removeu o nome de João

# print(nomes)


# frase = '    Se o produto ta caro,     não compra    '
# frase_crua = frase.split(',')

# frase_listada = []
# for i, frase in enumerate(frase_crua):
#     frase_listada.append(frase_crua[i].strip()) 
    
# print(frase_listada)
# print(frase_crua)
# frase_modificada = '**FAZUELI**'.join(frase_listada)
# print(frase_modificada)

