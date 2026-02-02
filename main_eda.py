# main_eda.py
import seaborn as sns
import matplotlib.pyplot as plt
from data_cleaner import limpiar_datos
from config import COLS_FEATURES

def ejecutar_eda():
    df = limpiar_datos() # Trae los datos sin fallos
    
    # Gráfico de Balanceo (Ejercicio 3.1)
    sns.countplot(x='target', data=df)
    plt.title("Balanceo de Clases")
    plt.show()

    # Matriz de Correlación (Ejercicio 3.2 - Multicolinealidad)
    plt.figure(figsize=(10,8))
    sns.heatmap(df[COLS_FEATURES + ['target']].corr(), annot=True, cmap='coolwarm')
    plt.title("Detección de Multicolinealidad")
    plt.show()

if __name__ == "__main__":
    ejecutar_eda()