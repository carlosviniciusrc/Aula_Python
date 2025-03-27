
#(Parte 1) *args para quantidade de argumentos não nomeados variáveis
"""
args = Argumentos não nomeados
* - *args (empacotamento e desempacotamento)

Em Python, *args é um mecanismo para passar um número variável 
de argumentos para uma função. Ele permite que você envie múltiplos 
valores sem precisar defini-los explicitamente na assinatura da função.

Como funciona *args?
O *args transforma os argumentos posicionais em uma tupla, 
permitindo que a função lide com um número desconhecido de entradas.
"""

# lembre-te de desempacotamento

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

# def soma(*args):
#     total = 0
#     for numero in args:
#         total += numero
#     return total

# somas = soma(5, 10, 15, 20)
# print(somas)


# (Parte 2) *args para quantidade de argumentos não nomeados variáveis

# Sum:
# Em Python, a função sum() é usada para calcular a 
# soma dos elementos de um iterável (como listas, tuplas e conjuntos).

def soma(*args):
    return sum(args)


soma2 = soma(1, 5, 5, 1)
print(soma2)