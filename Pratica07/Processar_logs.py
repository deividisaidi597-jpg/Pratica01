# Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de exercução constantes.

import pandas as pd


def Processar_Dados(nome_arquivo):
    # Lê o arquivo CSV
    df = pd.read_csv(nome_arquivo)

    # Calcula estatísticas
    media_tempo = df["tempo_execucao"].mean()
    desvio_padrao_tempo = df["tempo_execucao"].std()
    # Retorna os resultados
    return media_tempo, desvio_padrao_tempo


if __name__ == "__main__":
    arquivo = "logs.csv"
    media, desvio = Processar_Dados(arquivo)
    print(f"Média do tempo de execução: {media:.2f}")
    print(f"Desvio padrão do tempo de execução: {desvio:.2f}")
