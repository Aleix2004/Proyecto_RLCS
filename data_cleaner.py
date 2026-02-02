# data_cleaner.py
import pandas as pd
from config import RUTA_CSV

def limpiar_datos():
    df = pd.read_csv(RUTA_CSV)
    
    # 1. Encontrar fallos (Nulos)
    nulos = df.isnull().sum().sum()
    if nulos > 0:
        print(f"Advertencia: Se encontraron {nulos} valores nulos. Limpiando...")
        df = df.dropna()
    
    # 2. Corregir tipos de datos
    # Convertimos el target a numérico (0 y 1)
    df['target'] = df['winner'].astype(int)
    
    return df