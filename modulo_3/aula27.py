'''
Fatiamento de Strings
 0123456789
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade 
de caractres da str
'''

variavel = 'Olá mundo'
print(variavel[4])
print(variavel[-4])
print(variavel[4:])
print(variavel[:5])
print(variavel[4:8])
print(variavel[-9:-6])

# Função len
print(len(variavel)) # vai exibir a quantidade de caracteres
print(len(variavel[4:8]))

# Fatiamento

print(variavel[0:9:2]) #passo
print(variavel[-9:-6:-1])
print(variavel[::-1]) #invertendo caracteres

