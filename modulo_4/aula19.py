# Métodos úteis em set:

# add, update, clear, discard

s1 = set()

# add() -> Adiciona um elemento ao conjunto.
s1.add('Olá mundo')

# O método update() em set é usado para adicionar múltiplos elementos de uma 
# coleção (ou várias coleções) a um conjunto existente.
s1.update(('Vinicius', 4))

# Diferença entre remove e discard:
# remove() -> Remove um elemento. Gera erro se não existir
s1.remove(4)
# discard() -> Remove um elemento, não vai gerar erro se não existir.
s1.discard(1)

# clear() -> Remove todos os elementos do conjunto.
#s1.clear()

print(s1)