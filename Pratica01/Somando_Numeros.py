# 2- Calculadora de Soma
# Desenvolva um programa que soma dois números.
# Use as variáveis numero1 = 12 e numero2 = 14.
# O programa deve calcular a soma e exibir o resultado.

# Solicita ao usuário que digite o primeiro número e converte para inteiro
numero1 = int(input("Digite um numero: "))

# Solicita ao usuário que digite o segundo número e converte para inteiro
numero2 = int(input("Digite outro numero: "))

# Calcula a soma dos dois números
soma = numero1 + numero2

# Exibe o resultado da soma formatado
print("A soma de {} + {} = {}".format(numero1, numero2, soma))
