# Formatação de strings com o método format

a = 'A'
b = 'B'
c = 1.1
# string = 'a={}, b={}, c={}' # 0 1 2 
string = 'c={letra3}, a={0}, b={1}' # Na função você pode alterar a ordem dos valores
# Sempre ao definir a função colocar '.' e depois 'format'.
# formato = string.format(a, b, c) # a ordem padrão é  0 1 2
formato = string.format(a, b, letra3 =c) # Inserindo um parametro nomeado
# Observe a alterção na varivel
# Caso contrario o argumento'a' tivesse nomeado, você teria que atribuir o parametro nomeado para o restante dos argumentos
# Ex: formato = string.format(letra1 =a, b, c) -> formato = string.format(letra1 =a, letra2=b, letra3 =c)
print(formato)