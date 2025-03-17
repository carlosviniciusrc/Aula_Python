"""
Operação Ternária (Condicional de um linha)
<valor> if <condicao> else <outro valor>

Em Python, a operação ternária é uma forma concisa de escrever uma 
instrução if-else em uma única linha. 
A sintaxe é:

valor_se_verdadeiro if condição else valor_se_falso
"""

# print('Valor' if True else 'Outro valor')

condicao = 10 == 10 
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

digito = 10
novo_digito = digito if digito <= 9 else 0
novo_digito2 = 0 if digito > 9 else digito
print(novo_digito)
print(novo_digito2)