# Filtro de dados em list comprehension (filter)

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# ex1

lista = [n for n in range(10) if n < 5]
# print(lista)

# ✅ O que ele faz?
# range(10) → gera os números de 0 a 9 (intervalo que vai até 10,
# mas não inclui o 10).

# for n in range(10) → percorre cada número n desse intervalo.

# if n < 5 → filtra os números: só passa para
# a lista os que são menores que 5.

# [n ...] → monta uma nova lista contendo apenas os elementos
# que passaram pelo filtro.

# Aplicando em um dicionario

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
   {**produto, 'preco': produto['preco'] * 1.05}
   if produto['preco'] > 20 else {**produto}
   for produto in produtos
   if produto['preco'] >= 20
]

p(novos_produtos)