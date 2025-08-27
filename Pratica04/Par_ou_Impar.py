# Crie um programa que solicite ao usuário que insira números inteiros. O programa deve continuar solicitando números até que o usuário digite 'fim'. Para cada número inserido, o programa deve informar se é par ou ímpar. Se o usuário inserir algo que não seja um número inteiro, o programa deve
# informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.

Numero_Par = []
Numero_Impar = []

while True:
    try:
        entrada = input("Digite um numero ou digite 'fim' para finalizar: ")

        if entrada.lower() == "fim":
            print("Finalizando..")
            break
        entrada = int(entrada)
        if entrada % 2 == 0:
            Numero_Par.append(entrada)
            print(f"Numero {entrada} é Par")
            continue

        else:
            Numero_Impar.append(entrada)
            print(f"Numero {entrada} é Impar")
            continue

    except:
        print("ERROR: Só números são válidos!")

print("\nPrograma encerrado.")
print(f"Quantidade de números pares: {len(Numero_Par)}")
print(f"Quantidade de números ímpares: {len(Numero_Impar)}")
