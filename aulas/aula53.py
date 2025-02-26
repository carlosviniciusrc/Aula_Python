'''
Introdução ao empacotamento e desempacotamento
'''

lista = ['Carlos', 'Rafaella', 'Vinicius']

# Armazenando os elementos de uma tupla ou lista em variáveis individuais

# nome1, nome2, nome3 = lista 
# print(nome3) # 'Vinicius'

# OBS.: Para fazer esse tipo de armazenamento o numero de variaveis deve ter
# a mesma quantidade de valores, caso não seja haverá ERRO.

'''
Em uma situação você quer apenas pegar um nome e armazenar o resto.
Para isso utiliza-se '*' e o nome da variavel. Veja abaixo:
'''

# Esta pegando o primeiro valor e armazenando o resto.
# nome1, *resto = lista
# print(nome1, resto) # 'Carlos', ['Rafaella','Vinicius']

# OBS.: Em casos de trabalho em equipe muitos desenvolvedores utilizam o '_' para armazenar.
# nome1, *_ = lista
# print(nome1, _) # 'Carlos', ['Rafaella','Vinicius']

# Ex2 
_, nome2, _ = lista
print(nome2, _) # 'Rafaella', 'Vinicius'

#O *resto agrupa os valores restantes em uma lista.

# Outro exemplo:

primeiro, *meio, ultimo = [10, 20, 30, 40, 50]
print(primeiro)  # 10
print(meio)      # [20, 30, 40]
print(ultimo)    # 50
