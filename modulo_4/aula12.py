# Manipulando chaves e valores em dicionários
usuario = {
    'nome': 'Vinicius',
    'idade': 23,
    'altura': 1.7,
    'cidade': 'Fortaleza',
    'endereço': [
        {'rua': 'Barbosa', 'numero': 123},
    ]
}

pessoa = {}

# Adicionando valores
pessoa['nome'] = 'Emilly'
pessoa['sobrenome'] = 'Brito'

chave = 'idade'
pessoa[chave] = 23

# editando valores
pessoa['nome'] = 'Emilly Brito'

# Deletando valores
del pessoa['sobrenome']
print(pessoa)

# O método .get() é usado para acessar o valor de uma chave em um dicionário, 
# de forma segura. Diferente do acesso direto com [], ele não gera erro se a 
# chave não existir.
# Retorna None (ou um valor padrão, se você quiser)
# Em condições é interessante usar get e sempre usar com is e is not, 
# pois as vezes evita KeyError

# Ex.:

if pessoa.get('sobrenome') is None:
    print('não existe')
else:
    print(pessoa['sobrenome'])

#✅ Quando usar get()?

#- Quando não tem certeza se a chave existe
#- Quando quer evitar try/except
#- Quando quer retornar um valor padrão automático