'''
Repetições
while(enquanto)
Executa uma ação enqunto um condição for verdadeira
Loop infinito -> Quando um código não tem fim

O comando 'while' faz com que um conjunto de instruções seja executado enquanto uma 
condição é atendida. Quando o resultado dessa condição passa a ser falso, 
a execução do loop é interrompida.
'''

condição = True

while condição:
    nome = input('Qual o seu nome: ')
    print(f'O seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')

# Ex 2
contador = 0
while (contador < 5):
    print(contador)
    contador = contador + 1

# Neste código, enquanto a variável contador, inicializada com 0,
# for menor do que 5, as instruções das linhas 26 e 27 serão executadas.

# Observe que na linha 27 incrementamos o valor da variável contador,
# de forma que em algum momento seu valor igualará o número 5.
# Quando isso for verificado na linha 25, o laço será interrompido.
# Sem esse código, a condição de parada não será atingida, gerando
# o que é chamado de loop infinito. Evite que isso aconteça,
# pois leva ao congelamento e finalização da aplicação.