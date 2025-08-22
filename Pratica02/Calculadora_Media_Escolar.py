# 3- Calculadora de Média Escolar
# Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:
# Nota 1: 7.5
# Nota 2: 8.0
# Nota 3: 6.5
# O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

Nota_1 = 7.5
Nota_2 = 8.0
Nota_3 = 6.5
Resultado = (Nota_1 + Nota_2 + Nota_3) / 3

print(
    "Notas do aluno: \nNota 1: {:.2f} \nNota 2: {:.2f} \nNota 3: {:.2f} \nResultado final: {:.2f}".format(
        Nota_1, Nota_2, Nota_3, Resultado
    )
)
