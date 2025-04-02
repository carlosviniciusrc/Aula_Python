# Exercício com funções

# Crie funções que duplicam, triplicam e quadruplicam 
# o número recebido como parâmetro

# Modelo 1

def operador(func, numero):
    return func(numero)

def dup(x):
    return x * 2

def tri(y):
    return y * 3

def quad(z):
    return z * 4

resultado = operador(quad, 5)
print(resultado)


# modelo 2

def gerador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicador = gerador(2)
triplicador = gerador(3)
quadruplicador = gerador(4)

print(duplicador(2))
print(triplicador(2))
print(quadruplicador(2))