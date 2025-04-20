# Métodos úteis dos dicionários em Python

# Shallow Copy vs Deep Copy em dados mutáveis Python

# Em Python, quando você copia objetos mutáveis (como listas, dicionários,
# conjuntos), é importante saber se você está copiando o conteúdo ou só a 
# referência.

# Shallow Copy (Cópia rasa)

# Cria uma nova estrutura externa.
# Mas os objetos internos continuam apontando para os mesmos lugares.
# É como copiar a casca, mas compartilhar o recheio.
import copy

pessoa = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

# v1 = pessoa.copy()
# v1['c1'] = 5
# print(pessoa)
# print(v1)

# Deep Copy (Cópia profunda)

# Cria uma cópia completa e independente
# Tudo é duplicado: estrutura externa e interna

v1 = copy.deepcopy(pessoa)
v1['l1'][1] = 50

print(pessoa)
print(v1)