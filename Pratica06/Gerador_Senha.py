# Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.

import random
import string


def gerador_Senha(quantidade):
    caracters_uppercase = string.digits + string.ascii_letters + "!@#$%&*"
    senha = "".join(random.choice(caracters_uppercase) for _ in range(quantidade))
    return senha


quantidade = int(input("Digite o tamanho da sua senha que deseja: "))
senha = gerador_Senha(quantidade)
print(f"Sua senha gerada é: {senha}")
