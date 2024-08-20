# Precedência entre os operadores aritmeticos

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

conta_1 = 1 + 1 ** 5 + 5 # 7

conta_2 = (1 + 1) ** 5 + 5 # 37

conta_3 = (1 + 1) ** (5 + 5) # 1024

conta_4 = (1 + int(0.5 + 0.5)) ** (5 + 5) # 1024

print(conta_1)
print(conta_2)
print(conta_3)
print(conta_4)