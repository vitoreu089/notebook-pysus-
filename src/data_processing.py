import pandas as pd
import os
import numpy as np
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

caminho_bruto = os.path.join(BASE_DIR,"data","raw","dados_dengue_minas.parquet")

df = pd.read_parquet(caminho_bruto)

# pd.to_datetime converte o texto em formato de data oficial.
# errors='coerce' faz com que datas corrompidas fiquem vazias (NaT).
df['DT_NOTIFIC'] = pd.to_datetime(df['DT_NOTIFIC'], errors='coerce')
df['DT_SIN_PRI'] = pd.to_datetime(df['DT_SIN_PRI'], errors='coerce')

def corrigir_idade(codigo):
    if pd.isna(codigo):
        return np.nan #indica vazio

    cod_str = str(int(codigo))

    if len(cod_str) != 4:
        return np.nan

    unidade = cod_str[0]
    valor = int(cod_str[1:])

    if unidade == '4':
        return valor # anos
    elif unidade in ['2', '3']:
        return 0 # Meses e dias são arredondados para 0 anos
    else:
        return np.nan

df['NU_IDADE_N'] = df['NU_IDADE_N'].apply(corrigir_idade)

# exclui apenas as linhas onde a coluna da idade esta vazia
df = df.dropna(subset=['NU_IDADE_N'])

# desconsidera idades que provavelmente foram digitadas erradas
df = df[df['NU_IDADE_N'] <= 130]

# filtro para montes claros
# código IBGE de Montes Claros: 314330
df_moc = df[df['ID_MUNICIP'] == '314330'].copy()

# limpa espaços invisiveis
df_moc['CLASSI_FIN'] = df_moc['CLASSI_FIN'].astype(str).str.strip()

# implementa dicionario para diagnostico (melhora o tratamento de dados)
dicionario_dengue = {
    '10': 'Dengue Clássica', '10.0': 'Dengue Clássica',
    '11': 'Dengue com Alarme', '11.0': 'Dengue com Alarme',
    '12': 'Dengue Grave', '12.0': 'Dengue Grave',
    '5': 'Descartado', '5.0': 'Descartado',
    '8': 'Inconclusivo', '8.0': 'Inconclusivo'
}

df_moc['DIAGNOSTICO'] = df_moc['CLASSI_FIN'].map(dicionario_dengue)

# --- SALVANDO O RESULTADO FINAL ---
# Garante que a pasta processed existe
pasta_destino = os.path.join(BASE_DIR, "data", "processed")
os.makedirs(pasta_destino, exist_ok=True)

# Salva o dataframe de Montes Claros limpo
caminho_processado = os.path.join(pasta_destino, "dengue_moc_limpo.parquet")
df_moc.to_parquet(caminho_processado, index=False)
