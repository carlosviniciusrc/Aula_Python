# List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de iteraveis.

# O que é List Comprehension em Python?
# List comprehension é uma forma concisa e elegante de criar listas 
# a partir de iteráveis, usando uma única linha de código.

# Ela permite gerar novas listas aplicando uma expressão a cada elemento 
# de uma sequência ou outro iterável, podendo ainda incluir condições (if).

# ✅ Estrutura básica:
#     [expressão for item in iterável]

# print(list(range(0,20, 2))) # lista de números pares

# forma simples
# lista = []

# for numero in range(10):
#     lista.append(numero)
# print(lista)

# utilizando lista comprehension

lista = [numero * 2 for numero in range(10)]
print(lista)


