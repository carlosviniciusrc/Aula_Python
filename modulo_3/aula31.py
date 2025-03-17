'''
Flag (Bandeira) = Marca um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
'''
# v1 = 'a'

# print(id(v1)) # vai exibir a identidade da variavel


condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')


# Is true

# x = ["apple", "banana", "cherry"]

# y = x

# print(x is y)

# Is false

# x = ["apple", "banana", "cherry"]

# y = ["apple", "banana", "cherry"]

# print(x is y)