"""
CONSTANTE = "Variáveis" que nao podem mudar
Muitas condições de if (ruim)
    <- Contagem de complexidade(ruim)
"""
velocidade = 61  # velocidade atual do carro em movimento
posicao = 99  # Posição inicia do carro referenciado na rodovia (km 100)

RADAR_1 = 60  # Velocidade máxima permitida do radar 1
LOCAL_1 = 100  # local onde o radar se encontra
RADAR_RANGE = 1  # Distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1

multa_por_velocidade = posicao >= (LOCAL_1 - RADAR_RANGE) and \
    posicao <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = multa_por_velocidade and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print("Velocidade limite da rodovia excedida em radar 1")

if carro_multado_radar_1:
    print("Carro multado em radar 1")