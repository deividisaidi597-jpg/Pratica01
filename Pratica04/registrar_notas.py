# Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.

notas = []
while True:
    try:
        entrada = input("Digite a nota do aluno ou 'fim' encerrar: ")
        if entrada.lower() == "fim":
            break
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Por favor, digite uma nota de 0 a 10.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia da turma: {media:.2f}")
    print(f"\nTotal de notas válidas registradas: {len(notas)}")
else:
    print("\n Nemhuma nota válida foi registrada.")
