"""
Iterável -> str, range, etc
iterador -> quem sabe entregar um valor por vez
next -> me entrega o proximo valor
iter -> me entrege seu iterador 
"""
# Iter me entrega o objeto interador 
# texto = iter('Vini') #___iter__()

# print(texto)

# O next chama o proximo valor que estiver disponivel no iter
'''
print(next(texto)) # V
print(next(texto)) # I
print(next(texto)) # N
print(next(texto)) # I
print(next(texto)) # nesse proximo vai ter um erro, pois não tem outro valor
'''

# Como o for funciona por baixo dos panos? (next, iter, iterável e iterador)

#for letra in texto:
texto = 'vini' #iteravel
iterador = iter(texto) #iterador

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break