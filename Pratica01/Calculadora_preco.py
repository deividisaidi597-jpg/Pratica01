# 4- Calculadora de Preço Total
# Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:
# Nome do produto: "Cadeira Infantil"
# Preço unitário: R$ 12.40
# Quantidade: 3
# O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

# Define o nome do produto
nome_produto = "Cadeira Infantil"

# Define o preço unitário do produto
preco_unitario = 12.40

# Define a quantidade comprada
Qtd = 3

# Calcula o preço total da compra
preco_total = preco_unitario * Qtd

#Printando o resultados
print("Produto: {} \nPreço unitário: R$ {:.2f} \nQuantidade: {} \nValor total do produto: R${:.2f}".format(nome_produto,preco_unitario,Qtd,preco_total))