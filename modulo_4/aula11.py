"""
Dicionários em Python (tipo dict)
 Dicionários são estruturas de dados do tipo
 par de "chave" e "valor".
 Chaves podem ser consideradas como o "índice"
 que vimos na lista e podem ser de tipos imutáveis
 como: str, int, float, bool, tuple, etc.
 O valor pode ser de qualquer tipo, incluindo outro
 dicionário.
 Usamos as chaves - {} - ou a classe dict para criar
 dicionários.
 Imutáveis: str, int, float, bool, tuple
 Mutável: dict, list

🧪 Prática: Como Usar Dicionários
✅ Criando dicionários
# Forma tradicional

# pessoa = {
#    "nome": "Maria",
#    "idade": 30,
#    "cidade": "Recife"
#}

# Usando dict()

#pessoa2 = dict(nome="Carlos", idade=25, cidade="Salvador")
"""
# Forma mais utilizada é a que está abaixo, pois com dict() não é tão utilizado,
# apenas para conversões de dados

usuario = {
    'nome': 'Vinicius',
    'idade': 23,
    'altura': 1.67,
    'cidade': 'Fortaleza',
    'endereço': [
        {'rua': 'Barbosa', 'numero': 123},
    ]
}

# Acessando o Dicionario
print(usuario) # Vai exibir todas as informações
print(usuario['nome'], end='\n\n') # vai acessar apenas uma chave

# Teste 1
# vai fazer o loop para exibir todas as informções
for chave in usuario:
    print(chave, usuario[chave])