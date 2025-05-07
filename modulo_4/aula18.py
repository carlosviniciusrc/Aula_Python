# Sets são eficientes para remover valores duplicados
# de iteráveis.

# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

lista = [1, 2, 3, 4, 4, 1]
print(lista)

# Após a conversão da lista para set os valores duplicados vão ser removidos.
s1 = set(lista)
print(s1)

# Utilizando iteradores
lst = []
for i in s1:
    lst.append(i)

print(lst)