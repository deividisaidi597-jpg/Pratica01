# Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:
# A calculadora deve solicitar ao usuário que insira dois números e uma operação.
# As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
# O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
# Trate os seguintes erros:
# Entrada inválida (não numérica) para os números
# Divisão por zero
# Operação inválida
# Use try/except para capturar e tratar os erros apropriadamente.
# Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
# Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.


while True:

    try:
        N1 = float(input("Digite um numero: "))
        N2 = float(input("Digite outro numero: "))
        operacao = input("Digite a operação (+ , -, *, / ): ").strip()

        if operacao == "+":
            valor = N1 + N2
            print(f"Adição: {valor}")
            break

        elif operacao == "-":
            valor = N1 - N2
            print(f"Subtração: {valor}")
            break

        elif operacao == "*":
            valor = N1 * N2
            print(f"Multiplicação: {valor}")
            break

        elif operacao == "/":
            valor = N1 / N2
            print(f"Divisão: {valor}")
            break
        else:
            print("Operação inválida. Use apenas +, -, * ou /.\n")
            continue

    except ValueError:
        print("Erro: digite apenas números válidos.\n")
        continue
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero.\n")
        continue
