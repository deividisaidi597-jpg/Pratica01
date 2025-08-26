# 3- Calculadora de IMC
# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
# calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.
# < 18.5: classificacao = "Abaixo do peso"
# < 25: classificacao = "Peso normal"
#  < 30: classificacao = "Sobrepeso"
#  Para os demais cenários: classificacao = "Obeso"

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

IMC = peso / (altura**2)

if IMC < 18.5:
    classificacao = "Abaixo do peso"
elif IMC < 25:
    classificacao = "Peso normal"
elif IMC < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print("Seu IMC é : {:.1f} \nClassificação: {}".format(IMC, classificacao))
