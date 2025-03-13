"""
Imprecisão de ponto flutuante 
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
numero_1 = 0.7
numero_2 = 0.1
numero_3 = numero_1 + numero_2
print(numero_3)

# Para corrigir isso podemos usar o F-strings que formata para string e converte
print(f'{numero_3:.2f}') # resultado vai ser em string (0.80)

# Ou podemos usar a função round() que é usada para arredondar números para 
# um número específico de casas decimais.
# Sintaxe: round(número, casas_decimais)
print(round(numero_3, 2)) # 0.8

'''
Em outros casos para dados mais precisos podemos utilizar modulo Decimal

O módulo decimal do Python fornece operações matemáticas de alta precisão,
ideais para cálculos financeiros ou científicos onde a precisão é essencial.
'''
import decimal

numero_4 = decimal.Decimal(0.7)
numero_5 = decimal.Decimal(0.1)
numero_6 = numero_4 + numero_5
print(numero_6) # 0.7999999999999999611421941381

"""
Conclusão
- Se você precisa apenas exibir valores arredondados, round() pode ser suficiente.
- Se precisa de cálculos exatos (por exemplo, em finanças), use decimal.Decimal.
"""