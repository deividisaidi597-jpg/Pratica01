# Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto. Requisitos:
# Permitir que o usuário informe o preço do produto e o percentual de desconto.
# Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
# Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).


def Calcular_Desconto(preco, porcentual_desconto):
    desconto = preco * (porcentual_desconto / 100)
    preco_final = preco - desconto
    return preco_final


preco_original = float(input("Digite o preço do produto (Ex: 250,75): R$ "))
desconto = float(input("Digite o percentual de desconto (Ex: 15,5): "))

preco_com_desconto = Calcular_Desconto(preco_original, desconto)

print(
    f"O preço final com {desconto}% de desconto sobre R$ {preco_original:.2f} é R$ {preco_com_desconto:.2f}"
)
