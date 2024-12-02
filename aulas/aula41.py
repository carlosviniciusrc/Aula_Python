''' while/else'''

# string = 'Valor qualquer'

# i = 0

# while i < len(string):
#     letra = string[i]

#     # if letra == ' ':
#     #     break

#     print(letra)
#     i += 1
# else:
#     print('não teve break')
# print('fim do cod')


'''
    Em Python, o laço while pode ser acompanhado de um bloco else. 
    O bloco else em um loop while será executado somente quando a 
    condição do while for avaliada como False. Se o loop for interrompido 
    por um comando break, o bloco else não será executado.
'''

'''
O bloco else após um while é útil quando você quer executar um código 
apenas se o loop completar normalmente (sem interrupção por break).
Se o loop for interrompido com break, o bloco else será ignorado.
'''

# Busca ou Verificação de Condição
numeros = [1, 3, 5, 7, 9]
procurado = 7
indice = 0

while indice < len(numeros):
    if numeros[indice] == procurado:
        print(f"Número {procurado} encontrado na posição {indice}.")
        break
    indice += 1
else:
    print(f"Número {procurado} não encontrado.")
