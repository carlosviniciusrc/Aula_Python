'''
For in com listas
'''
lista = ['Carlos', 'Rafaella', 'Vinicius']

# for nome in lista:
#     print(nome, type(nome))


# Exercicio exiba os indices da lista

# indice = 0

# for nomes in lista:
#     print(indice, nomes)
#     indice += 1

# resolução 2 :
lista.append('Maria')
lista.insert(1, 'Augusto')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))