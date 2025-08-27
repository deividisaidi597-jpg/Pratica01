# Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.

while True:
    senha = input("Digite sua senha ou digite 'sair' para finalizar ")

    if senha.lower() == "sair":
        print("Programa encerrado.")
        break

    if len(senha) < 8:
        print("Senha Fraca. A senha deve ter pelo menos 8 caracteres.")
        continue

    if not any(caracter.isdigit() for caracter in senha):
        print("Senha Fraca. A senha precisa ter pelo menos um número.")
        continue

    if not any(caracter.isalpha() for caracter in senha):
        print("Senha Fraca. A senha precisa ter pelo menos uma letra")
        continue

    if not any(caracter.isupper() for caracter in senha):
        print("Senha Fraca. A senha precisa ter pelo menos uma letra maiúscula.")
        continue

    print("Senha forte e válida!")
    break
