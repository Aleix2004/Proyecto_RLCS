# data_loader.py
import pandas as pd
from config import RUTA_CSV

def cargar_y_limpiar():
    if not os.path.exists(RUTA_CSV):
        raise FileNotFoundError(f"No se encontró el archivo en: {RUTA_CSV}")
    
    df = pd.read_csv(RUTA_CSV)
    
    # Creamos la variable objetivo (target)
    if 'winner' in df.columns:
        df['target'] = df['winner'].astype(int)
    else:
        # Fallback por si acaso
        df['target'] = (df['core_goals'] > 0).astype(int)
        
    return df