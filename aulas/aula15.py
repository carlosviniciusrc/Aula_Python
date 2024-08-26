# Usando a função Input para coletar dados

nome = input('Qual o seu nome? ')

print(f'O seu nome é {nome}')


# Soma de numeros

numero_1 = input('Digite um numero: ')
numero_2 = input('Digite outro numero: ')

# Como você quer saber a soma de dois numeros, voce faz uma check dos valores,
# pois caso você coloque um sring ja pode dar erro no seu código.

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

# Após isso os numeros vão passar por um typecasting(conversão) para int

print(f'A soma dos dois numeros é {int_numero_1 + int_numero_2}')

# Valor de X

A = input('Digite o valor de A: ')
B = input('Digite o valor de B: ')

int_A = int(A)
int_B = int(B)

X = int_A + int_B

print(f'X = {X}')

# area = n * raio²

raio = float(input())

n = 3.14159

area = n * (raio ** 2)


print(f'A = {area:.4f}')

# media

a = float(input())
b = float(input())

media = (a * 3.5 + b * 7.5) / 11

print(f'MEDIA = {media:.5f}')
