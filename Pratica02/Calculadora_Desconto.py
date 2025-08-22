# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:
# Nome do produto: "Camiseta"
# Preço original: R$ 50.00
# Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

Nome_Produto = "Camiseta"
Preco_Original = 50.00
Desconto = 20

Valor_Desconto = Preco_Original * (20 / 100)
Preco_Final = Preco_Original - Valor_Desconto

print(
    "Produto: {} \nPreço original: R$ {:.2f} \nDesconto: {}% \nValor do Desconto: R${:.2f} \nPreço Total: R${:.2f}".format(
        Nome_Produto, Preco_Original, Desconto, Valor_Desconto, Preco_Final
    )
)
