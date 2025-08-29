# Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.

import requests


def obter_Usuario_Aleatorio():
    url = "https://randomuser.me/api/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()["results"][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados["email"]
        pais = dados["location"]["country"]
        return f"\nNome: {nome} \nEmail:{email}\n{pais}"
    except requests.RequestException as e:
        return f"Erro ao obter usuário aleatório: {e}"


print("Gerando um usuário aletório...")
usuario = obter_Usuario_Aleatorio()
print(usuario)
