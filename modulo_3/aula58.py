"""
split  e join com list e str
split - divide uma string
join - une uma string
"""
# A função split() divide uma string em uma lista de substrings,
# usando um separador específico (por padrão, espaços).

frase = '   Se o produto ta caro,   não compra      '
lista_de_frases_crua = frase.split(',')

"""
Manipulação de Strings em Python com strip(), rstrip() e lstrip()

A função strip() remove espaços em branco do início e do fim da string.

A função rstrip() remove apenas espaços (ou caracteres) do final da string.

A função lstrip() remove apenas espaços (ou caracteres) do início da string.
"""
lista_de_frases = []
for i, frase in enumerate(lista_de_frases_crua):
    lista_de_frases.append(lista_de_frases_crua[i].strip())

print(lista_de_frases_crua)
print(lista_de_frases)




# O método join() é usado para juntar elementos de uma lista (ou outra sequência iterável) 
# em uma única string, separando-os por um delimitador específico.
# Sintaxe - separador.join(iterável)
frase_unida = '****'.join(lista_de_frases)
print(frase_unida)