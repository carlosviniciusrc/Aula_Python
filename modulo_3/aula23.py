# operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if not senha:
    print('Você não digitou nada')
else:
    print('Entrar')


print(not 0) #False
print(not 1) #True
