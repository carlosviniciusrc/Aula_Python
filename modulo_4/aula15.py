# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Carlos Vinicius',
    'sobrenome': 'Rodrigues',
    'idade': 23,
    'Cidade': 'Fortaleza'
}

# Pop
# Remover uma chave específica do dicionário e retornar seu valor.
# Se a chave não existir, você pode passar um valor padrão pra evitar erro.

idade = pessoa.pop('idade')
print(idade)
print(pessoa)

# Popitem()
# Remover e retornar o último item inserido no dicionário

ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)

# Update
# Atualizar o dicionário com novos pares chave:valor.
# Se a chave já existir, o valor é substituído.

novos_dados = {'idade': 24, 'lastname': 'Cardoso'}
pessoa.update(novos_dados)
print( end='\n')
print(pessoa)

