# Revisão dia 17/03

# Gerador de CPF

"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# Primeiro Digito
cpf = '74682489070'
nove_digitos = cpf[:9]
contador1 = 10

resultado1 = 0
for digito in nove_digitos:
    resultado1 += int(digito) * contador1
    contador1 -= 1

digito1 = (resultado1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0

# Segundo Digito

dez_digitos = nove_digitos + str(digito1)
contador2 = 11

resultado2 = 0
for digito in dez_digitos:
    resultado2 += int(digito) * contador2
    contador2 -= 1

digito2 = (resultado2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0

cpf_complete = nove_digitos + str(digito1) + str(digito2)
print(cpf_complete)


# Basico de função 

# def novo_mundo():
#     print('Hello World')

# novo_mundo()

# # Para chamar uma função utilizamos 'def', após definimos o nome da função 
# # e dentro do parenteses passamos o parâmetro e abaixo o bloco de codigo da
# # exibição da função

# def soma(x,y):
#     print(f'{x=} {y=} | x + y = ', x + y )

# soma(1,2)
# soma(x = -5, y = 2)
