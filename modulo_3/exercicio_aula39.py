"""
Iterando strings com while
"""

nome = 'Carlos Vinicius'
indice = 0
nova_string = ''

# Vai exibir uma letra abaixo da outra

# while indice < len(nome):
#     print(nome[indice])
#     indice += 1

#Vai exibir a variavel nome
while indice < len(nome):
    letra = nome[indice]
    nova_string += letra 
    indice += 1
    
print(nova_string)
