# 4- Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

Temperatura = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").upper()
destino = input("Unidade de destino (C, F ou K): ").upper()

if origem == destino:
    resultado = Temperatura
elif origem == "C" and destino == "F":
    resultado = Temperatura * 9 / 5 + 32
elif origem == "F" and destino == "C":
    resultado = (Temperatura - 32) * 5 / 9
elif origem == "C" and destino == "K":
    resultado = Temperatura + 273.15
elif origem == "K" and destino == "C":
    resultado = Temperatura - 273.15
elif origem == "F" and destino == "K":
    resultado = (Temperatura - 32) * 5 / 9 + 273.15
elif origem == "K" and destino == "F":
    resultado = (Temperatura - 273.15) * 9 / 5 + 32
else:
    print("Conversão inválida")
    resultado = None

if resultado is not None:
    print(f"{Temperatura}°{origem} = {resultado:.2f}°{destino}")
