# Operadores lógicos in (entre) e not in (não está entre)
# Strings são iteráveis
# Iteráveis são objetos capazes de retornar seus membros um de cada vez - eles podem ser iterados. 
# As estruturas de dados incorporadas populares do Python, como listas, tuplas e conjuntos, são qualificadas como iteráveis.

# 0 1 2 3 4 5 6 7
# V i n i c i u s
# -8-7-6-5-4-3-2-1

# nome = 'Vinicius'
# print(nome[2]) vai verificar a ordem das letras de 0 a 7
# print(nome[-2]) vai verificar a ordem das letras de -8 a -1

# print('n' in nome) # está perguntando se 'n' esta entre o valor da variavel nome.
# print('b' in nome) #false
# print('Vini' in nome) #true
# print(10 * '-')
# # Ex de not in:

# print('g' not in nome) # esta perguntando se não está entre o nome
# print('cius' not in nome)


nome = input('Digite seu nome: ')
encontrar = input('Digite o que você que encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
    