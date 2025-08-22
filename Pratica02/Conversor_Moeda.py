# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
# Valor em reais: R$ 100.00
# Taxa do dólar: R$ 5.60
# Taxa do euro: R$ 6.60
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

Valor_reais = 100.00
Taxa_Dolar = 5.60
Taxa_Euro = 6.60

Valor_Dolar = 100.00 / 5.60
Valor_Euro = 100.00 / 6.60

print(
    "Valor em Reais: R$ {:.2f} \nValor em Dolar: US$ {:.2f} \nValor em Euro: € {:.2f}".format(
        Valor_reais, Valor_Dolar, Valor_Euro
    )
)
