from sqlalchemy import create_engine
import pandas as pd


usuario = ''
senha = ''
host = ''
porta = '5432'
banco_de_dados = ''
tabela = ''

conexao_string = f"postgresql://{usuario}:{senha}@{host}:{porta}/{banco_de_dados}"

engine = create_engine(conexao_string)

print(f"Iniciando carregamento dos dados! Aguarde...")

df = pd.read_csv("./transformacao/precos_ativos.csv", sep=',')
df.to_sql(tabela, con=engine, if_exists='replace', index=False)

print(f"Carregamento dos dados finalizados na tabela: {banco_de_dados}/{tabela}!")
