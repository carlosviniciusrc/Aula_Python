"""Calculadora com while"""

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+ - * /): ')

    # Um flag para utilizar para cchecar o coding
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        # Vai converter os números para floar
        # A variavel numeros_validos vai chegar o flag
        num_1_float = float(numero_1)
        num_2_float = float(numero_1)
        numeros_validos = True
    except:
        # Caso aconteça algum erro ele vai seguir par o if
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os numeros digitados são inválidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Estamos verificando sua conta...')

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
    else:
        print('Tem algo de errado aí')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    #lower() é utilizado para deixar a letra minuscula
    #startswith('s') vai definir com qual letra ou numero vai começar
    
    if sair is True:
        break