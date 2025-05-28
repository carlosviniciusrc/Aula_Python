# Empacotamento e desempacotamento de dicionários + *args e **kwargs

# Empacotamento e desempacotamento - simples

a, b = 1, 2
a, b = b, a
# print(a, b)

# Empacotamento e desempacotamento - dicionarios:


# teste

pessoa = {
    'nome': 'Carlos',
    'sobrenome': 'Vinicius'
}

# a, b = pessoa.values()
# print(a, b)

# for chave, valor in pessoa.items():
#     print(valor)

# Empacotamento de dicionários em Python se refere principalmente ao uso
# do operador ** (chamado de "unpacking operator" ou "desempacotamento")
# para passar ou combinar dicionários.

outros_dados = { 
    'idade': 20,
    'Altura': 1.67
}

pessoa_completa = {**pessoa, **outros_dados}

# for chave, valor in pessoa_completa.items():
#     print(chave, valor)


# Kwargs

# Quando usar **kwargs?
# ✅ Quando você não sabe de antemão quantos argumentos nomeados a função precisa aceitar.
# ✅ Para criar funções flexíveis e extensíveis.
# ✅ Muito comum em frameworks (Flask, Django) para receber várias opções.

# Boas práticas:
# Use **kwargs apenas quando realmente quiser aceitar argumentos variados.

# Documente claramente que sua função aceita **kwargs e o que ela espera como chave.

# Evite abuso, pois pode tornar o código menos legível e mais difícil de depurar.

def desempacotador(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

desempacotador(nome='vini', idade= 23)
print()
desempacotador(**pessoa_completa)

# Kwargs e args

def teste(*args, **kwargs):
    print('Não Nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

config = {
    'config1': 1,
    'config2': 2,
    'config3': 3,
    'config4': 4,
}

teste(10,20,**config)

# Ex 1

def saudacao(nome,idade):
    print(f'Olá, {nome}. Você tem {idade} anos')

dados = {
    'nome': 'Vinicius',
    'idade': 24
}

saudacao(**dados)



