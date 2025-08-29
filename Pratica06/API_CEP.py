# Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.


import requests


def consultar_Cep(cep):
    URL = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(URL)
        response.raise_for_status()
        dados = response.json()

        if "erro" in dados:
            return "CEP não encontrado."

        logradouro = dados["logradouro"]
        bairro = dados["bairro"]
        cidade = dados["localidade"]
        estado = dados["uf"]

        return f"\nLogradouro: {logradouro}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {estado}"

    except requests.RequestException as e:
        print(f"Erro ao consultar o CEP: {e}")


cep = input("Digite seu CEP: ").replace("-", "").strip()
endereco = consultar_Cep(cep)
print(endereco)
