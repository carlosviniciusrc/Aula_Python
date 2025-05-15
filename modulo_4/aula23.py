# convertendo funções para lambda

def executa(funcao, *args):
    return funcao(*args)


def soma(x,y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


# Em lambda

somas = executa(soma, 2, 3)
somas_lambda = executa(lambda x, y: x + y, 2, 3)
print(somas_lambda)
print(somas)

duplica = cria_multiplicador(2)
print(duplica(5))

duplica_lambda = executa(
    lambda m: lambda n: n * m, 2
)

print(duplica_lambda(5))