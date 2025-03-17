# Introdução ao for / in - estrutura de repetição para coisas finitas

texto = 'Python'

# i = 0

# while i < len(texto):
#     print(texto[i], i)

#     i += 1

nova_string = ''

for letra in texto:
    nova_string += f'*{letra}'
    print(letra)
print(nova_string)


