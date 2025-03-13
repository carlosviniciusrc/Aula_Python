"""
Introdução a funções(def) em python
Funções são trechos de código usados para
replicar determinada acão ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).

Os termos parâmetro e argumento são frequentemente usados de forma intercambiável, mas têm significados distintos em Python.

1. Parâmetro
São as variáveis declaradas dentro dos parênteses na definição de uma função.
Funcionam como espaços reservados para receber valores quando a função for chamada.

2. Argumento
São os valores reais passados para a função quando ela é chamada.
São atribuídos aos parâmetros definidos na função.

Resumo
Parâmetro 	Variável usada na definição da função.
Argumento 	Valor passado na chamada da função.
"""



# def declara a função e 'Print' é nome da function

# def Print():
#     print('Varias')
#     print('Varias')
#     print('Varias')
#     print('Varias')

# Só chamamos a função de você colocar o nome dela com ().
# Print()

def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)
imprimir(4, 5, 6)

# Quando você faz a chamada da função e não passa um argumento para ele, vai
# aparecer um erro, por isso você em certos casos pode passa um valor para o
# parametro
def saudacao(nome):
    print(f'Olá, {nome}!')

saudacao('Vini')
saudacao('Carlos')

