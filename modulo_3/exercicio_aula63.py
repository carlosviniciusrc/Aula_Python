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

import os
import re
# O módulo sys em Python fornece funções e variáveis que interagem 
# com o interpretador da linguagem. Ele permite manipular entradas, 
# saídas, argumentos da linha de comando, entre outras funcionalidades.
import sys

while True:
    # O método .replace() em Python é usado para substituir partes de uma string por outra. 
    # Ele retorna uma nova string com as substituições feitas, pois as strings em Python são imutáveis.
    # Aqui está utilizando o metodo re da biblioteca.
    # r'[^0-9]' nessa opção vamos substituir qualquer coisa de 0 a 9 por nada ('')
    
    # Quebra da expressão r'[^0-9]':
    # r'' → String bruta (raw string)

    # Evita problemas com barras invertidas \, garantindo que sejam interpretadas literalmente.
    # [...] → Classe de caracteres

    # Define um conjunto de caracteres que podem ser correspondidos.
    # ^ (Circunflexo dentro de [...]) → Negação

    # Quando colocado no início dentro dos colchetes, significa "NÃO".
    # [^0-9] significa "qualquer caractere que NÃO seja um número".
    # 0-9 → Intervalo de números

    # Representa os dígitos de 0 a 9.
    
    entrada = input('Digite seu CPF: ')
    cpf_enviado = re.sub(r'[^0-9]', '', entrada)
    # Aqui vamos realizar o fatiamento da string
    nove_digitos = cpf_enviado[:9]
    # Aqui teremos o contador regressivo para o lop
    contador_regressivo_1 = 10

    # Flag para evitar caracteres antigos
    # Como o algoritmo valida uma sequencia de numeros de 0 a 9
    # No caso esse trecho do codigo vai quebrar essa senquencia
    entrada_sequencial =  entrada == entrada[0] * len(entrada)

    if entrada_sequencial:
        print('Você enviou dados senquenciais')
        sys.exit() # trocar por continue no loop

    resultado_1 = 0
    for digito in nove_digitos:
        resultado_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1

    digito_1 = (resultado_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    # Para buscar o segundo digito do CPF:
    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_2 = 0
    for digito in dez_digitos:
        resultado_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digito_2 = (resultado_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    # Validação CPF

    cpf_calculado = f'{nove_digitos}{digito_1}{digito_2}'

    if cpf_calculado == cpf_enviado:
        os.system('cls')
        print(f'{cpf_enviado} é válido')
    else:
        os.system('cls')
        print('CPF é Invalido')


# Possiveis problemas no codigo:

#   O primeiro problema seria de o usuario colocxar ',' e '-' no seu cpf 
#   para isso utilizamos o método '.replace'.

#   O método .replace() em Python é usado para substituir partes de uma string 
    #por outra. Ele retorna uma nova string com as substituições feitas, pois as
    #strings em Python são imutáveis.

#   No segunda opção é trocar o .replace para 're' que é um biblioteca.

#   O segundo problema é utilizar caracteres repetidos, pois no código um sequencia
#   de numeros de [0-9], pode dar CPF válido.
#   Para isso usamos uma flag que vai impedir de isso ocorrer.


