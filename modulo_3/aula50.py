"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

# Nesse arquivo vamos ver Clear e Insert

lista = [10, 20, 30, 40]

# insert(): Adiciona um elemento em uma posição específica.

# A sintaxe é "lista.insert(indice, elemento)"
lista.insert(0,9)

# O método .clear() é usado para remover todos os elementos de uma lista, deixando-a vazia, mas sem apagar a variável da memória.

#lista.clear()

# Fazendo a mescla

nomes = ["Ana", "Bruno", "Carlos", "Pedro", "João"]

nomes.append("Vinicius") # adicionou o nome 
nomes.pop() # Como eu tinha adicionado por ultimo "Vinicius", ele vai apagar 
nomes.append("Vini")
nomes.insert(0, "Emilly") # Adicinou o nome "Emilly no indice 0"

print(nomes)

lista2 = ['pera', 'uva', 'maçã', 'banana']

lista2.append('melão')
lista2.pop()
lista2.insert(0, 'abacate')
lista2.pop()
del lista2[-1]

print(lista2)