#  while + while (laços internos)

# Repetições
# while(enquanto)
# Executa uma ação enqunto um condição for verdadeira
# Loop infinito -> Quando um código não tem fim

# use o Debbuger para entender o codigo
qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1
