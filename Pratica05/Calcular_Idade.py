# Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

from datetime import date


def Calcular_Idade_dias(Ano_Nascimento):
    ano_atual = date.today().year
    idade = ano_atual - Ano_Nascimento
    dias = idade * 365
    return dias


Ano_Nascimento = int(input("Digite o seu ano de nascimento: "))

resultado_dias = Calcular_Idade_dias(Ano_Nascimento)
print(f"Você tem aproximadamente {resultado_dias:.0f} dias de vida.")
