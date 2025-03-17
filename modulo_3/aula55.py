"""
enumerate - enumera iteráveis (índices)

O enumerate() é uma função embutida do Python que adiciona um contador
a um iterável (como listas, tuplas ou strings), retornando um objeto enumerado.
Isso facilita a obtenção do índice e do valor simultaneamente dentro de um loop for.
"""

lista = ['Carlos', 'Rafaella', 'Vinicius']

lista_enumerada = enumerate(lista)

for a, b in lista_enumerada:
    print(a, b)

# importante:
# utilizar o enumerate em uma variavel você só pode utilizar ele um vez, pois
# seu valores se esgotam, por isso é melhor utilizar fora de variavel. Veja abaixo:

for item in enumerate(lista):
    print(item)
    

# 1️⃣ Sintaxe do enumerate()

# enumerate(iterável, start=0)

# iterável: Qualquer sequência (lista, tupla, string, etc.).
# start: Valor inicial do índice (por padrão, começa em 0).
 