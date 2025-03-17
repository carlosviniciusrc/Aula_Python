"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    #definição
    print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z) # x=1 y=2 | x + y = 3

# Argumento não nomeado
soma(1, 2, 6)
# Argumento nomeado
soma(y=2,x=1, z=6)
# Argumentos nomeados e não nomeados
# Você pode utilizar os dois, mas sempre que nomear um o proximo tem que está
# nomeado, pois pode da erro de sintaxe.
soma(1, 4, z=3)
soma(7, y= 6, z= 5) # valido
#soma(y= 7,  6, z= 5) # não valido

# Geralmente você sempre vai chamar tudo nomeado e não nomeado