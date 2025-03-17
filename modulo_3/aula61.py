# Desempacotamento em chamadas de funções

string = 'ABCD'
lista = ['Maria', 'Helena', 'Eduarda']
tupla = 'Python', 'é', 'legal'

print(*lista)

'''
 Explicação:
O operador * (desempacotamento) faz com que os elementos da lista sejam 
passados individualmente como argumentos para a função print(). 
Isso é equivalente a escrever:
'''
print('Maria', 'Helena', 'Eduarda') # Maria Helena Eduarda

# OU

for nome in lista:
    print(nome, end= ' ') # Maria Helena Eduarda
    

print('\n')
# Por padrão, print() separa os elementos 
# com um espaço (sep=' '), mas você pode mudar isso:
print(*lista, sep=", ") # Maria, Helena, Eduarda

# Esse desempacotamento (*) é útil para passar elementos de uma lista como
# argumentos de funções ou para formatar a saída de maneira flexível! 🚀


