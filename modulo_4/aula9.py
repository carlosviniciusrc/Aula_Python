"""
Closure e funções que retornam outras funções

O que é Closure em Python?
Uma closure em Python ocorre quando uma função interna "lembra" 
e pode acessar variáveis de seu escopo externo, mesmo após esse 
escopo ter sido finalizado.

Isso é possível porque funções em Python são objetos de primeira classe, 
o que significa que podem ser retornadas como valores e ainda manter acesso
 às variáveis do escopo em que foram criadas.

🔹 Quando usar closures?
✅ Para criar funções especializadas sem precisar repetir código.
✅ Para encapsular dados de forma semelhante a uma classe.
✅ Para construir decoradores em Python.
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

nomes = 'Vinicius', 'Maria', 'João', 'Paulo'

for nome in nomes:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))