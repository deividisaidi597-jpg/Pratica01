# Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.


import json


def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo_json:
            dados = json.load(arquivo_json)
            print(dados)
    except FileNotFoundError:
        print("Arquivo não encontrado")


def escrever_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, "w") as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
        print(f"Dados salvos com sucesso em {nome_arquivo}")
    except Exception as e:
        print(f"Erro {e} ao salvar o arquivo.")


dados = [["Jose", 24, "Vitoria de santo antao"], ["Lucas", 30, "Rio de janeiro"]]

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo JSON: ").strip()
    escrever_json(nome_arquivo, dados)
    ler_json(nome_arquivo)
