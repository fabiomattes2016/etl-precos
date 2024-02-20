import pandas as pd
import os


diretorio = "./extracao"
dados = []

print("Iniciando transformação de dados! Aguarde...")

for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.csv'):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        df = pd.read_csv(caminho_arquivo, sep=',')
        df.dropna(inplace=True)
        df['preco'] = df['preco'].str.replace('.', '').str.replace(',', '.').astype(float)
        dados.append(df)

consolidado = pd.concat(dados)

pasta_destino = './transformacao/'
nome_arquivo = 'precos_ativos.csv'
caminho_completo = pasta_destino + nome_arquivo

consolidado.to_csv(caminho_completo, index=False, sep=',')

print(f"Dados exportados para o arquivo {caminho_completo}")
