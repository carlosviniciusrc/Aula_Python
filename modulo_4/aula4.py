"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.

O escopo de funções em Python determina onde uma variável 
pode ser acessada dentro do código. Ele define os limites 
de visibilidade e existência das variáveis.

A palavra-chave global é usada dentro de uma função para 
indicar que uma variável pertence ao escopo global 
e não ao escopo local da função. Isso permite modificar 
a variável global dentro da função.

callstack -> é uma estrutura de dados usada pelo Python para rastrear
a execução das funções no programa. Sempre que uma função é chamada,
ela é adicionada à pilha. Quando a função termina, ela é removida da pilha.

Para compreender o codigo seguinte utilize o debbuger
"""
x = 1

def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)
    
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)