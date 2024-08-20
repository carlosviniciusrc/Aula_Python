# f-strings (Formatação de Srings)

# Funiciona você colocando um 'f' no inico de onde você quer habilitar a formatação
teste_1 = f'Meu nome é Vinicius e tenho 23 anos.'

print(teste_1)

# Você também pode exibir valores de variavel no f-string.
nome_1 = 'Vinicius'
idade_1 = 23
teste_2 = f'Meu nome é {nome_1} e tenho {idade_1} anos.'

print(teste_2)

# O 'f' também é utilizado para definir o numero de casas decimais
altura_1 = 1.50
dinheiro = 2000
teste_3 = f'Maria tem altura de {altura_1:.2f}' # Esse ':.2f' vai definir o numero de casas após a virgula.
teste_4 = f'Maria vai ao shopping e tem apenas {dinheiro:,.2f} reais' # Também pode ser utinlizado para converter valores de moedas colocando ':,.xf'
print(teste_3)
print(teste_4, end='\n\n')

# Calculo do IMC com f-string
nome = 'Carlos Vinicius'
idade = 23
peso = 65
altura = 1.67
imc = peso / (altura * altura)

linha_1 = f'Meu nome é {nome} e tenho {idade} anos. O meu peso é {peso}kg e tenho a altura de {altura}m'
linha_2 = f'O valor do meu IMC é {imc:.2f}'

print(linha_1)
print(linha_2)






