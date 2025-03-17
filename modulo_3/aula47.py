"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""


import os

palavra_secreta = 'vini'
letras_acertadas = ''
numero_tentativas = 0


# O laço infinito para repetir a letre no acerto, ou erro.
while True:
    letra_digitada = input('Digite um letra: ') # vai ler a letra

    numero_tentativas += 1

    # Vai verificar se o usuario digitou mais de uma letra
    if len(letra_digitada) > 1: 
        print('Digite apenas uma letra')
        continue
    
    # Vai verificar se tem palavras relacionadas a palavra secreta
    # Com isso, vai atribuir a letra digitada as letras certas
    if letra_digitada in palavra_secreta:
         letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada:', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('PARABÉNS! VOCÊ CONSEGUIU!')
        print('A palavra secreta é', palavra_secreta)
        print(f'O seu número de tentativas foi de {numero_tentativas} vezes')
        letras_acertadas = ''
        numero_tentativas = 0