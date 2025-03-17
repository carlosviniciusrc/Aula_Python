"""
Tipo tupla - uma lista imutavel

O que são Tuplas em Python?
Uma tupla é uma estrutura de dados imutável que pode armazenar múltiplos
valores em uma única variável.

🔹 Características das Tuplas:
✔ Imutáveis (não podem ser alteradas após a criação)
✔ Podem armazenar qualquer tipo de dado (int, float, string, listas, etc.)
✔ Aceitam elementos duplicados
✔ Usam parênteses () para serem definidas
"""

# 1️⃣ Criando Tuplas

# Tupla com números
numeros = 10, 20, 30
print(numeros)

# Tupla com tipos diferentes
dados = ("João", 25, True)

# Tupla vazia
vazia = ()



'''
 - Tupla com um único elemento (precisa da vírgula no final)
Importante: Se não colocar a vírgula em uma tupla de um único elemento,
ela será considerada um tipo de dado normal.
'''
unica = (5,) # ou 5,
print(unica)

# 2️⃣ Acessando Elementos da Tupla

cores = ("vermelho", "azul", "verde")

print(cores[0])  # vermelho
print(cores[1])  # azul
print(cores[-1]) # verde (último elemento)

# Convertendo Lista para Tuplas
tuple(cores)

# Convertendo Tuplas para Lista
list(numeros)
