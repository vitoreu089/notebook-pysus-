import os
import glob
import pandas as pd
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from pysus.online_data import SINAN

def executar_coleta():
    
    SINAN.download('DENG', 2024)
    SINAN.download('DENG', 2025)
    
    #caminho dinamico
    pasta_usuario_pysus = os.path.join(os.path.expanduser("~"), "pysus", "**", "*.parquet")
    arquivos_parquet = glob.glob(pasta_usuario_pysus, recursive=True)
    
    if arquivos_parquet:
        pasta_destino = os.path.join(BASE_DIR, "data", "raw")
        os.makedirs(pasta_destino, exist_ok=True)
        
        colunas = ['TP_NOT', 'DT_NOTIFIC', 'DT_SIN_PRI', 'CS_SEXO', 'NU_IDADE_N', 'CLASSI_FIN', 'EVOLUCAO', 'SG_UF_NOT', 'ID_MUNICIP']
        
        dfs = []
        for arquivo in arquivos_parquet:
            print(f"Lendo e filtrando o arquivo: {os.path.basename(arquivo)}")
            df_ano = pd.read_parquet(arquivo, columns=colunas, filters=[('SG_UF_NOT', '==', '31')])
            dfs.append(df_ano)
        
        df_bruto_total = pd.concat(dfs, ignore_index=True)
        caminho_final = os.path.join(pasta_destino, "dados_dengue_minas.parquet")
        df_bruto_total.to_parquet(caminho_final, index=False)

if __name__ == "__main__":
    executar_coleta()