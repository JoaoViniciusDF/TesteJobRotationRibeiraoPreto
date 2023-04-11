# Distância entre Ribeirão Preto e Franca em km
distancia = 100

# Velocidade do carro em km/h
velocidade_carro = 110

# Velocidade do caminhão em km/h
velocidade_caminhao = 80

# Tempo adicional dos pedágios para o caminhão em horas
tempo_adicional_pedagios = 2 * 5 / 60

# Cálculo do tempo de viagem do carro até o ponto de encontro
tempo_carro = distancia / velocidade_carro

# Cálculo do tempo de viagem do caminhão até o ponto de encontro, considerando o tempo adicional dos pedágios
tempo_caminhao = (distancia / velocidade_caminhao) + tempo_adicional_pedagios

# Verificação e comparação dos tempos de viagem
if tempo_carro < tempo_caminhao:
    print("O carro estará mais próximo da cidade de Ribeirão Preto quando se cruzarem na rodovia.")
elif tempo_caminhao < tempo_carro:
    print("O caminhão estará mais próximo da cidade de Ribeirão Preto quando se cruzarem na rodovia.")
else:
    print("O carro e o caminhão chegarão ao ponto de encontro na mesma hora.")
