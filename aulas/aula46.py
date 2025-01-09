for i in range(10):
    if i == 2:
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1,3):
        print(i, j)
else:
    print('For completo com sucesso')

# Você foi contratado para criar um programa que analisa as notas de uma
# turma de estudantes. O programa deve:
# Receber uma lista de notas.
# Calcular a média das notas.
# Determinar a nota mais alta e a nota mais baixa.
# Contar quantas notas estão acima da média.

notas = [8.5, 9.0, 6.5, 7.0, 10.0, 5.5, 8.0]

soma_notas = 0
nota_mais_baixa = notas[0]
nota_mais_alta = notas[0]

for nota in notas:
    soma_notas += nota
    if nota > nota_mais_alta:
        nota_mais_alta = nota
    if nota < nota_mais_baixa:
        nota_mais_baixa = nota

media_notas = soma_notas / len(notas)

acima_da_media = 0

for nota in notas:
    if nota > media_notas:
        acima_da_media += 1


print(f'A nota mais alta é {nota_mais_alta}')
print(f'A media das notas é {media_notas:.2f}')
print(f'A nota mais baixa é {nota_mais_baixa}')
print(f'O total de notas acima da média é {acima_da_media}')

# for com while

for i in range(1,4):
    contador_0 = 0
    while contador_0 < 3:
        print(f'linha {i}, coluna {contador_0}')
        contador_0 += 1

# Desenvolva um programa que use um loop for para iterar sobre uma lista de
# números e calcule a soma de todos os números.

lista = [1, 2, 3, 4, 5, 6]

# while
contador_1 = 0
i = 0
soma = 0

while contador_1 < 6:
    soma = soma + lista[i]
    i = i + 1
    contador_1 +=1

print(soma)

# for
valor = 0

for numero in lista:
    valor += numero

print(valor)


# Tabuada de multiplicação
# while True:
#     try:
#         numero = int(input('Digite o numero que você quer saber a tabuada de multiplicação: '))

#         for i in range(11):
#             produto = numero * i
#             print(f'{numero} * {i} = {produto}')
#     except:
#         print('Digite apenas números')
#         continue


# Contar vogais em uma string

# frase = input('Digite uma frase: ').lower()

# vogais = 'aeiou'
# contador = 0

# for letra in frase:
#     if letra in vogais:
#         contador += 1

# print(f'O númeor de vogais na frase é de {contador}')

# Números pares e ímpares

# for i in range (1,51):

#     if i % 2 == 0:
#         print(f'{i} é um numero par')
#     else:
#         print(f'{i} é numero impar')

# Nível Avançado

# Fatorial de um número

numero = int(input('Informe um número para exibir o fatorial: '))

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}.")



