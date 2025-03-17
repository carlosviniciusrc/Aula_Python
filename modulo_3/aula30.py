'''
CONSTANTE = "Variáveis que não vão mudar"
Muitas comdições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
'''

velocidade = 61 # velocidade atual carro
local_carro = 100 # local em que o carro está na estrada

# CONSTANTES
RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

# if velocidade > RADAR_1:
#     print('Velocidade do carro um passou do radar 1')

# # O barra invertida serve para quebrar a linha para dar continuação ao código
# if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
#     local_carro<- (LOCAL_1 + RADAR_RANGE) and \
#     velocidade > RADAR_1:
#         print('O carro foi multado')

# Simplificando e deixando mais 'limpo'

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')