# data_transformer.py
from sklearn.preprocessing import StandardScaler
from config import COLS_FEATURES

def transformar_datos(df):
    """
    Aplica el escalado estándar a las variables explicativas.
    """
    scaler = StandardScaler()
    
    # Creamos una copia para no alterar el original
    df_transformado = df.copy()
    
    # Aplicamos el escalado (StandardScaler)
    # Esto convierte los valores a una escala común (Z-score)
    df_transformado[COLS_FEATURES] = scaler.fit_transform(df[COLS_FEATURES])
    
    print("Transformación: Escalado de variables completado.")
    return df_transformado, scaler