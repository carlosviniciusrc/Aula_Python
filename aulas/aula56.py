"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
minha_lista = []

while True:

    print('Selecione uma opção')
    opcao = input('[I]inserir [A]apagar [L]listar: ').lower()

    if opcao not in 'ial':
        print('Insira os valores sugeridos')
        continue

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        minha_lista.append(valor)
        os.system('cls')
        continue
    elif opcao == 'a':
        os.system('cls')
        try:
            item_apagado = input('Escolha um item para apagar: ')
            minha_lista.remove(item_apagado)
            os.system('cls')
            continue
        except:
            print('Não foi possivel encontrar esse valor')
            continue
    elif opcao == 'l':
        for numero, item in enumerate(minha_lista):
            print(numero, item)



