# List comprehension com mais de um for

# Fazendo sem List comprehension

lista1 = []

for x in range(3):
    for y in range(3):
        lista1.append((x,y))

# print(lista1)

# Fazendo com List comprehension

lista2 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista2)