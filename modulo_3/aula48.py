"""
Listas em Python
Tipo list = Mutavel
Suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, deel, clear, extend, +
"""

#         01234
#        -54321
string = 'ABCDE'  # 5 caracteres

# Em Booleno o valor de uma lista vazia é o mesmo de uma string vazia
# lista = []
# string1 = ''


#print(bool(lista)) # false
#print(bool(string1)) # false

# O type list suportar vários valores de qualquer tipo
#         0     1      2     3      4
#        -5    -4      -3    -2     -1
lista = [123, 'vini', True, 4.5 ,  []]
#        int    str   bool  float  list

# Pode acessar elemetos individuais
print(lista[1])
print(lista[-3])

# Podemos fazer alteração na lista
lista[-3] = 'Carlos'
print(lista[-3], type(lista), type(lista[-3]))



