import pandas as pd
import os

def load_and_audit_pollution_data(csv_path):
    """
    Carrega o CSV 'raw' e prepara para o dashboard.
    """
    # Verifica se o arquivo RAW existe
    if not os.path.exists(csv_path):
        return None, f"ERRO: Arquivo original não encontrado em {csv_path}"

    try:
        df = pd.read_csv(csv_path)
        
        # Mapeamento exato do seu Get-Content
        # Date,City,CO,NO2,SO2,O3,PM2.5,PM10,Type
        required_cols = ['Date', 'Type', 'PM2.5'] 
        
        missing = [col for col in required_cols if col not in df.columns]
        if missing:
            return None, f"ERRO: Colunas ausentes no CSV: {missing}"

        # Limpeza básica
        df = df.dropna(subset=['PM2.5', 'Type'])
        df['Date'] = pd.to_datetime(df['Date'])
        
        return df, "✅ Dataset RAW carregado e auditado!"
        
    except Exception as e:
        return None, f"ERRO Crítico: {str(e)}"

def get_stats_by_zone(df):
    """Retorna estatísticas comparativas entre Industrial e Residencial"""
    stats = df.groupby('Area_Type')['Pollutant_Level'].agg(['mean', 'max', 'min']).to_dict('index')
    return stats