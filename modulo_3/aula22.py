# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condiçõa verdadeira avalia toda expressõa como verdadeira.
# Se qualquer valor for considerado verdadeiro, a expressão
# interira será avaliada naquele valor.
# São considerados falsy (que você ja viu)
# 0 0.0 '' false
# Também existe o tipo None que é usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Digite sua senha: ')

senha_permitida = '1234'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


# Avaliação de curto circuito:

print(0 or False or 0 or 'abc' or True)

# Exemplo de simolificação

senha3 = input('senha: ') or 'sem senha' # é utilizado para simplificar seu codigo
print(senha3)
