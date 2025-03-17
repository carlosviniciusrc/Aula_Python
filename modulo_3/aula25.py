"""
Interpolação básica de Strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'vinicius'
preco = 1000.8545544
variavel = '%s, o preço é R$%.2f' % (nome, preco) # O modelo da interpolação
# Sempre após utilizar % e o parentese para declarar as variaveis.
print(variavel)
