# Análise Epidemiológica da Dengue em Montes Claros (MG) com PySUS

Este projeto realiza uma Análise Exploratória de Dados (EDA) sobre registros de notificações de dengue no município de Montes Claros, em Minas Gerais, utilizando dados públicos do SINAN acessados por meio da biblioteca PySUS.

O objetivo principal é reorganizar e refatorar uma análise exploratória inicial, transformando-a em um projeto de Ciência de Dados mais estruturado, reproduzível e documentado.

---

## Objetivo da Análise

A análise busca investigar padrões presentes nos registros de dengue em Montes Claros nos anos de 2024 e 2025, considerando aspectos temporais, demográficos e diagnósticos.

As principais perguntas analíticas são:

1. Como os casos de dengue se distribuíram ao longo do tempo em Montes Claros?
2. Quais grupos demográficos concentraram maior número de notificações?
3. Existe diferença no intervalo entre início dos sintomas e notificação entre os sexos?
4. Qual foi a distribuição dos diagnósticos finais registrados no período analisado?

---

## Fonte dos Dados

Os dados foram obtidos a partir do SINAN (Sistema de Informação de Agravos de Notificação), disponibilizado pelo DATASUS.

A coleta foi realizada utilizando a biblioteca `PySUS`, com registros de dengue referentes aos anos de 2024 e 2025.

Devido a limitações de compatibilidade observadas no uso do PySUS em ambiente Windows, a etapa de coleta foi executada em ambiente Linux por meio do WSL.

---

## Ambiente de Execução

O projeto foi desenvolvido utilizando:

- WSL com Ubuntu
- Python 3.11.15
- Ambiente virtual (`venv`)
- PySUS 1.0.1
- Jupyter Notebook / VS Code

A utilização do WSL foi adotada para garantir maior compatibilidade com o PySUS e suas dependências, especialmente durante a etapa de coleta dos dados.

---

## Estrutura do Projeto

```text
projeto_dengue_pysus/
│
├── data/
│   ├── raw/
│   │   └── dados_dengue_minas.parquet
│   │
│   └── processed/
│       └── dengue_moc_limpo.parquet
│
├── notebooks/
│   └── analise_pysus.ipynb
│
├── src/
│   ├── data_collection.py
│   └── data_processing.py
│
├── requirements.txt
├── README.md
└── .gitignore
````

---

## Descrição das Pastas

### `data/raw`

Contém os dados brutos coletados via PySUS, antes das etapas de limpeza e tratamento.

### `data/processed`

Contém os dados já tratados e filtrados para o município de Montes Claros.

### `src`

Contém os scripts responsáveis pelas etapas de coleta e processamento dos dados.

* `data_collection.py`: realiza a coleta dos dados via PySUS;
* `data_processing.py`: realiza limpeza, tratamento, filtragem e geração do dataset processado.

### `notebooks`

Contém o notebook principal da análise exploratória.

---

## Como Executar o Projeto

### 1. Acessar o ambiente WSL

No terminal do Windows, abra o WSL:

```bash
wsl
```

Depois, acesse a pasta do projeto:

```bash
cd ~/projeto_dengue_pysus
```

---

### 2. Criar o ambiente virtual

```bash
python3.11 -m venv .venv
```

---

### 3. Ativar o ambiente virtual

```bash
source .venv/bin/activate
```

---

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 5. Executar a coleta dos dados

```bash
python src/data_collection.py
```

Esse script coleta os dados de dengue via PySUS e armazena o arquivo bruto em:

```text
data/raw/dados_dengue_minas.parquet
```

---

### 6. Executar o processamento dos dados

```bash
python src/data_processing.py
```

Esse script realiza o tratamento dos dados e gera o arquivo processado em:

```text
data/processed/dengue_moc_limpo.parquet
```

---

### 7. Abrir o notebook

Com o ambiente virtual ativado, abra o VS Code pelo WSL:

```bash
code .
```

Depois, abra o notebook:

```text
notebooks/analise_pysus.ipynb
```

Selecione o kernel da `.venv` e execute as células do notebook.

---

## Pipeline do Projeto

O fluxo do projeto segue a seguinte lógica:

```text
Coleta via PySUS
        ↓
Dados brutos em data/raw
        ↓
Processamento e limpeza
        ↓
Dados tratados em data/processed
        ↓
Análise exploratória no notebook
```

Essa separação permite maior organização, facilita a reexecução das etapas e evita que o notebook concentre todo o processo de coleta, limpeza e análise.

---

## Principais Etapas de Tratamento

Durante o processamento dos dados, foram realizadas as seguintes etapas:

* conversão de colunas de data para o formato `datetime`;
* tratamento da variável de idade codificada pelo SINAN;
* remoção de registros com idade ausente ou inconsistente;
* filtragem geográfica para o município de Montes Claros;
* padronização de categorias textuais;
* mapeamento dos códigos de diagnóstico final para categorias interpretáveis;
* armazenamento do dataset tratado em formato `.parquet`.

---

## Bibliotecas Utilizadas

As principais bibliotecas utilizadas foram:

* `pandas`
* `numpy`
* `matplotlib`
* `pysus`
* `pyarrow`
* `ipykernel`

As versões e dependências estão descritas no arquivo:

```text
requirements.txt
```

---

## Observações sobre Reprodutibilidade

A etapa de coleta foi testada em ambiente Linux via WSL, pois o PySUS apresentou problemas de compatibilidade em ambiente Windows, especialmente com versões mais recentes do Python e dependências associadas.

Por esse motivo, recomenda-se executar o projeto em:

```text
WSL / Linux + Python 3.11 + PySUS 1.0.1
```

Os arquivos `.parquet` gerados nas etapas de coleta e processamento são armazenados localmente para facilitar a reprodução da análise e evitar dependência de downloads repetidos durante a execução do notebook.

---

## Limitações

A análise possui caráter exploratório e deve ser interpretada considerando limitações dos dados de notificação, como:

* possibilidade de subnotificação;
* campos ausentes ou inconsistentes;
* atrasos de atualização;
* diferença entre casos notificados e casos confirmados;
* ausência de variáveis externas, como clima, saneamento, renda ou ações de controle vetorial.

Dessa forma, os resultados não devem ser interpretados como relações causais, mas como padrões descritivos observados nos registros disponíveis.

---

## Autor

**Vitor Emanuel Santos Cruz**

Email: `vitoremanuelsc089@gmail.com`

