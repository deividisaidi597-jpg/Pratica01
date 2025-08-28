# Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

from datetime import date


def Calcular_Idade_dias(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    dias = idade * 365
    return dias


ano_nascimento = int(input("Digite o seu ano de nascimento: "))

resultado_dias = Calcular_Idade_dias(ano_nascimento)
print(f"Você tem aproximadamente {resultado_dias:.0f} dias de vida.")
