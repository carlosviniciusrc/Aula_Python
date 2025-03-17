'''
Introdução ao try/except
Try -> tentar execitar o codigo
Except -> Ocorreu algum erro ao tentar executar
'''
# Ex 1:
numero_str = input('Vou dobrar o número que voce digitar: ')

# if numero_str.isdigit(): #isdigit checa se o usuario digitou apenas numeros e retorna umvalor booleano
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2}')
# else:
#     print('Isso não é um número')

# Ex 2:

# As vezes o úsuario pode errar colocando uma strng ao invés de numero. Com isso,
# utilizamos o Try e Except.
try:
    numero_float = float(numero_str) # caso dê um erro pulamos para o except
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except: # Aqui estabelecemos o que vai aprecer no erro do usuário. para não aprecer o erro automatico de valuerro do sistema.
    print('Isso não é um número')



