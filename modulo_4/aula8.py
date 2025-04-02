"""
Higher Order Functions
Funções de primeira classe

Em Python, funções de primeira classe significam que funções podem 
ser tratadas como qualquer outro objeto. Isso inclui armazená-las 
em variáveis, passá-las como argumentos para outras funções e retorná-las 
como valores.

O que isso permite?
"""


# Atribuir funções a variáveis

def apresentacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

v = executa(apresentacao, 'Seja Bem-Vindo', 'Vinicius')
print(v)

# Passar funções como argumentos

def aplicar_operacao(x, y, func):
    return func(x, y)

def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

print(aplicar_operacao(5, 3, soma))  # Saída: 8
print(aplicar_operacao(5, 3, multiplicacao))  # Saída: 15


# Retornar funções de outras funções 

def saudacao_personalizada(saudacao):
    def mensagem(nome):
        return f"{saudacao}, {nome}!"
    return mensagem

ola = saudacao_personalizada("Olá")
print(ola("Maria"))  # Saída: Olá, Maria!



