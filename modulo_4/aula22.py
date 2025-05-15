# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

# Em Python, tanto sort() quanto sorted() são usados para ordenar elementos, 
# mas há diferenças importantes entre eles:

# sort()
# Tipo: método de listas.
# Modifica a lista original (ordenando os elementos in-place).
# Retorna: None.

# sorted()
# Tipo: função built-in (funciona com qualquer iterável, como listas, tuplas, dicionários, etc.).
# Não modifica o iterável original, faz uma cópia rasa.
# Retorna: uma nova lista ordenada.

# Se quiser ordenar sem alterar os dados originais, use sorted(). 
# Se quiser economizar memória e alterar diretamente uma lista, use sort(). 
# Ambos aceitam os parâmetros key= e reverse= para personalizar a ordenação.
# Se quiser, posso mostrar um exemplo usando key também.

# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)


# Ordenando a lista por função

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def ordena(item):
    # Nesse return está pedindo para a lista ser 
    # ordenada a partir da chave 'nome'.
    return item['nome']

# O parâmetro key em sort() permite personalizar a forma como os elementos 
# são comparados ao ordenar. Você passa uma função para key, e essa função 
# será aplicada a cada elemento antes da comparação.
lista.sort(key=ordena)

# Exibindo a lista ordenada
for itens in lista:
    print(itens)

# Ordenando por lambda

# Em Python, lambda é uma maneira de criar funções pequenas
# e anônimas (sem nome) em uma única linha.

# Essas funções geralmente são usadas quando você precisa de uma função rápida 
# e simples, que será usada só uma vez, especialmente como argumento para outras 
# funções.

# 🧱 Estrutura da lambda

# lambda argumentos: expressão

# lambda → palavra-chave para criar a função.
# argumentos → como os parâmetros de uma função.
# expressão → o que será retornado (não precisa escrever return).

# Com sort()
lista.sort(key=lambda item: item['nome'])

# Com sorted()

def exibidor(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibidor(l1)
exibidor(l2)

# Ex 2

# função comum
def quadrado(x):
    return x * x

# Função lambda

f = lambda x: x * x

print(f(5))