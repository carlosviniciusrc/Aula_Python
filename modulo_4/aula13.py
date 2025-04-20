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
    'idade': 23
}

# len - Vai exibir a quantidade de chaves no dicionario
print(len(pessoa)) # ou print(pessoa.__len__())

# keys - Ele retorna uma view com todas as chaves do dicionário.
print(pessoa.keys()) # voce pode fazer conversão pata list ou tuple

# values - Vai retornar os valores das chaves
print(pessoa.values())

# items -  Vai exibir todos os itens do dicionário com seus valores.
print(pessoa.items())

# setdefault é meio ninja — ele serve tanto para pegar o valor de uma chave 
# quanto para definir um valor padrão se a chave não existir.
print(pessoa.setdefault('cidade', 'Fortaleza'))

# Os métodos .get() e .setdefault() dos dicionários em Python são parecidos,
# mas têm uma diferença essencial:

# .get(): somente leitura

# Usado para acessar o valor de uma chave de forma segura.
# Não modifica o dicionário.

# .setdefault(): leitura + criação se necessário

#Acessa o valor se a chave existir.
#Cria a chave com um valor padrão se ela não existir.