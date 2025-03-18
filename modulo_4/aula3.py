"""
Valores padrão para parâmetros 
Ao definir uma função, os parametros podem 
ter valores padrão. Caso o valor não seja 
enviado para o parametro, o valor padrão será usado.

É muito comum a gente criar funções em Python e definir 
um valor para aquele determinado parâmetro como sendo um não valor, ou seja.
Eu estou definindo o parâmetro de destaque, mas ele ainda não tem nenhum valor 
e isso me permite usar:

        is e is note
Refatorar: editar seu codigo

E muitos casos precisamos fazer alterações em nosso codigo, para isso as vezes
já deixamos declaros alguns parametros.

Usar 'None' como valor padrão evita efeitos colaterais inesperados ao 
trabalhar com valores mutáveis ou calculados dinamicamente.

  Resumo:
- 0 é um valor numérico válido, enquanto None representa a ausência de valor.
- 0 pode ser usado em operações matemáticas, None não.
- Ambos são False em contextos booleanos, mas None é mais usado para indicar 
um estado indefinido ou um valor ausente.
"""

# No seguinte caso adicionamos 'z', mas como 0 é um valor false em booleano
# vamos utilizar None.

# Nesta condição estamos perguntando de Z não é None, caso for None vai 
# aparecer apenas o valor de X e Y.
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=} | x + y + z =', x + y + z)
    else:
        print(f'{x=} {y=} | x + y =', x + y)

soma(1, 2, 0)

