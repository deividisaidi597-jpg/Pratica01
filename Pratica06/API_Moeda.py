# Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.


import requests


def consultar_Code(moeda):
    par = f"{moeda.upper()}"
    url = f"https://economia.awesomeapi.com.br/json/last/{par}"
    print(url)
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        info = dados[f"{par}BRL"]
        nome = info.get("name")
        valor_atual = info.get("bid")
        maximo = info.get("high")
        minimo = info.get("low")
        data = info.get("create_date")

        return (
            f"\nMoeda: {nome}"
            f"\nValor Atual: R$ {valor_atual}"
            f"\nMáximo do dia: R$ {maximo}"
            f"\nMínimo do dia: R$ {minimo}"
            f"\nÚltima atualização: {data}"
        )

    except requests.RequestException as e:
        print(f"Erro ao consultar o codigo: {e}")


codigo_moeda = (
    input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").strip().upper()
)
resultado = consultar_Code(codigo_moeda)
print(resultado)
