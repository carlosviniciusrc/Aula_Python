# Mapeamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos1 = [
    produto['nome']
    for produto in produtos
]

# print(novos_produtos1)
# print(*novos_produtos1, sep='\n')

# mapeando criando um novo dicionario

novos_produtos2 = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos2, sep='\n')


# 1. ✅ O que faz {**produto, 'preco': produto['preco'] * 1.05}?

# Essa é uma técnica chamada "desempacotamento de dicionário".
# {**produto} → copia todas as chaves e valores do dicionário produto.
# , 'preco': produto['preco'] * 1.05 → sobrescreve o valor da chave 'preco' com um aumento de 5%.

# ✅ 3. O que significa o if ... else ... dentro da list comprehension?

# Se o preço do produto for maior que 20, ele cria um novo dicionário com o preço aumentado.

# Caso contrário, apenas copia o dicionário original sem modificar.