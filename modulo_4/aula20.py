# Operadores úteis:

conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}

# união '|' união (union) - Une
conjunto3 = conjunto1 | conjunto2
print('união:',conjunto3)

# intersecção '&' (intersection) -: Itens presentes em ambos
conjunto4 = conjunto1 & conjunto2
print('intersecção:',conjunto4)

# diferença '-' -> itens presentes apenas no set da esquerda
conjunto5 = conjunto1 - conjunto2 # retorna: 1
conjunto6 = conjunto2 - conjunto1 # retorna: 4

# diferença simétrica '^' -> Itens que não estão em ambos
conjunto7 = conjunto1 ^ conjunto2
print('simétrica:',conjunto7)
