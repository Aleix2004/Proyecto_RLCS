# data_transformer.py
from sklearn.preprocessing import StandardScaler
from config import COLS_FEATURES

def transformar_datos(df):
    scaler = StandardScaler()
    
    # Escalamos las variables explicativas para que tengan media 0 y varianza 1
    df_escalado = df.copy()
    df_escalado[COLS_FEATURES] = scaler.fit_transform(df[COLS_FEATURES])
    
    return df_escalado