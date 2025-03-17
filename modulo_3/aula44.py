"""
- Sintaxe básica do For:

for variável in sequência:
    Bloco de código a ser repetido

variável: Representa o valor atual da iteração e assume um novo valor a cada ciclo.
sequência: Pode ser uma lista, tupla, string, range ou qualquer objeto iterável.
"""

# Iterando sobre uma string:

texto = 'Python'

for letra in texto:
    print(letra)


# For + Range
# range -> range(start, stop, step) // (inicio, fim, pular)

numeros = range(0, 100, 2)

for numero in numeros:
    print(numero)

# Percorrendo listas

frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print(fruta)




