# main_preparacion.py
from data_cleaner import limpiar_datos
from data_transformer import transformar_datos
from config import COLS_FEATURES

def ejecutar_preparacion():
    # 1. Limpiamos (Ejercicio 3/5.1)
    df_limpio = limpiar_datos()
    
    # 2. Transformamos (Ejercicio 5.3)
    df_final, _ = transformar_datos(df_limpio)
    
    print("\n--- COMPARACIÓN DE ESCALAS (Primeras 5 filas) ---")
    print("\nDatos Originales (Goles vs Boost):")
    print(df_limpio[COLS_FEATURES].head())
    
    print("\nDatos Escalados (Todo en la misma escala):")
    print(df_final[COLS_FEATURES].head())

if __name__ == "__main__":
    ejecutar_preparacion()