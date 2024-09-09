# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão 
# interira será avaliada naquele valor.
# São considerados falsy (que você ja viu)
# 0 0.0 '' false
# Também existe o tipo None que é usado para represntar um valor 

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Digite sua senha: ')

senha_permitida = '1234'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


# Avaliação de curto circuito:

print(True and False and True)