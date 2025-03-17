"""
Listas em Python
Tipo list = Mutavel
Suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append, insert, pop, deel, clear, extend, +

Crate read Update   Delete 
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)
"""

# Como na aula anterior vimos metodos para mudar os indices da lista e exibir.
# Nessa aula vamos ver as operações com lista 

# Operações com lista

# Append(): Adiciona um elemento ao final da lista.
numeros = [1, 2, 3, 4, 5]

numeros.append(6) # Adicionou o 6
numeros.append(7) # Adicionou o 7
print(numeros)


# Del: Remove um elemento ou fatia da lista.
lista = [10, 20, 30, 40]

del lista[2]
print(lista) # Removeu o 30

# Pop(): Remove um elemento ao final da lista por padrão, mas pode se remover qualquer
# Item da lista atribuindo seu indice

nomes = ["Ana", "Bruno", "Carlos", "Pedro", "João"]

nomes.pop() # Removeu o nome de João

#Aqui estamos removendo qualquer item da lista apenas indicando seu indice
nomes.pop() # Removeu o nome de Bruno
print(nomes)

# Mesclando tudo

compras_do_mes = ["maçã", "Arroz", "Feijão", "Frango", "Macarrão", "Temperos"]

# No momento foi identificado que não é necessario comprar maçã e sim laranjas para fazer suco

del compras_do_mes[0] # Ou poderia usar o .pop()
compras_do_mes.append("laranja")

print(compras_do_mes)