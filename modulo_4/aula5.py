"""
Retorno de valores das funções (return)

Em Python, o return é usado em funções para devolver um valor 
ao código que chamou a função. Isso permite reutilizar os resultados 
das funções em diferentes partes do programa.

Diferença entre print() e return
🔹 print() apenas exibe um valor na tela, mas não retorna nada para 
ser reutilizado.
🔹 return devolve o valor para ser usado em outra parte do código.
"""

def soma(x, y):
   if x > 10:
        return [10, 20]
   
   return x + y

soma1 = soma(2, 2)
soma2 = soma(3, 2)
soma3 = soma(11, 55)
print(soma1)
print(soma2)
print(soma3)
print(soma(15,35))

# Diferença entre print() e return

def soma(a, b):
    print(a + b)  # Apenas exibe o resultado, sem retornar

resultado = soma(3, 7)
print(resultado)  # Saída: 10 \n None (pois a função não retornou nada)
# Aqui, soma() apenas imprime o resultado, e resultado fica como None.

# ✅ Solução correta usando return:

def soma(a, b):
    return a + b  # Agora retorna o valor corretamente

resultado = soma(3, 7)
print(resultado)  # Saída: 10

