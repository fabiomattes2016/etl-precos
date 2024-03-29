# ETL de Preços de Ativos

Este projeto consiste em um ETL (Extração, Transformação e Carregamento) desenvolvido em Python para a manipulação de dados de preços de ativos. O processo é dividido em três principais etapas: extração dos dados, transformação dos mesmos conforme necessário e carregamento dos dados transformados em um banco de dados PostgreSQL.

## Ferramentas Utilizadas

- **Python 3.11**: Interpretador python usado no projeto
- **Selenium**: Utilizado na etapa de extração para navegar e obter dados de páginas web.
- **Pandas**: Empregado na etapa de transformação para manipular e preparar os dados.
- **SQLAlchemy**: Usado para facilitar a conexão com o banco de dados e o carregamento dos dados.
- **PostgreSQL**: O sistema de gerenciamento de banco de dados onde os dados são armazenados.
- **psycopg2**: Adaptador de banco de dados PostgreSQL para Python, utilizado junto com SQLAlchemy.

## Configuração Inicial

Antes de executar o projeto, é necessário alterar os dados de conexão com o seu banco no arquivo `carregamento.py`. Edite as linhas de 5 a 10 com suas informações de conexão ao banco de dados PostgreSQL.

## Como Executar

Para executar o projeto, siga os passos abaixo.

Instale as depêndencias do projeto:

```powershell
pip install -r requirements.txt
```

Extração dos dados:

```powershell
python extracao.py
```

Transformação dos dados:

```powershell
python transformacao.py
```

Carregamento dos dados no banco:

```powershell
python carregamento.py
```

Siga estas etapas para realizar o processo completo de ETL. Certifique-se de que todas as dependências estão instaladas no seu ambiente virtual antes de iniciar o processo.
