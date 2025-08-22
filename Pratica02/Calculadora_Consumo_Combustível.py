# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:
# Distância percorrida: 300 km
# Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

Distancia_Percorrida = 300
Combustivel_Gasto = 25

Consumo_Medio = Distancia_Percorrida / Combustivel_Gasto

print(
    "Distância percorrida: {:.2f} km \nCombustível gasto: {} l \nConsumo Médio: {:.1f} km/l".format(
        Distancia_Percorrida, Combustivel_Gasto, Consumo_Medio
    )
)
