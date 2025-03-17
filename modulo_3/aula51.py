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
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]


# Concatenção de listas com '+':

# A concatenação de listas no Python é feita usando o operador +,
# que cria uma nova lista combinando os elementos das listas originais.
lista_c = lista_a + lista_b
print(lista_c)

#✅ Vantagens: Simples e direto.
#❌ Desvantagem: Cria uma nova lista, não modifica as listas originais.

# Método .extend():
'''
O método .extend() não retorna uma nova lista, ele modifica 
a lista original e retorna 'None', caso esteja em uma variavel.
Pois está ação não cria um novo valor, mas altera diretamente
na lista que deseja extender
'''
lista_a.extend(lista_b)
print(lista_a)


"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_x = ['Luiz', 'Maria', 1, True, 1.2]
lista_y = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_x)
print(lista_y)