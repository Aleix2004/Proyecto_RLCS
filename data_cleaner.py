import pandas as pd
from config import RUTA_CSV

def limpiar_datos():
    df = pd.read_csv(RUTA_CSV)
    
    print("\n--- INFORME DE CALIDAD DE DATOS ---")
    
    # 1. Encontrar Nulos
    nulos = df.isnull().sum().sum()
    print(f"- Valores nulos encontrados: {nulos}")
    
    # 2. Encontrar Duplicados
    duplicados = df.duplicated().sum()
    print(f"- Filas duplicadas: {duplicados}")
    
    # Limpieza: Borrar nulos y duplicados si los hay
    df = df.dropna().drop_duplicates()
    
    # 3. Corregir tipos (Target)
    df['target'] = df['winner'].astype(int)
    
    print("Limpieza completada con éxito.")
    return df