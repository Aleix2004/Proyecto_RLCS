# main_diagnostico.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from data_cleaner import limpiar_datos
from data_transformer import transformar_datos
from config import COLS_FEATURES

def ejecutar_diagnostico():
    # Preparación rápida
    df = limpiar_datos()
    df_final, _ = transformar_datos(df)
    X = df_final[COLS_FEATURES]
    y = df_final['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    modelo = LogisticRegression()
    modelo.fit(X_train, y_train)
    
    # --- VISUALIZACIONES EJERCICIO 9 ---
    
    # 1. Probabilidades Predichas (Histograma)
    probs = modelo.predict_proba(X_test)[:, 1] # Probabilidad de ganar (clase 1)
    plt.figure(figsize=(8, 5))
    sns.histplot(probs, bins=20, kde=True, color='purple')
    plt.title('Distribución de Probabilidades de Victoria')
    plt.xlabel('Probabilidad Predicha (0 a 1)')
    plt.ylabel('Frecuencia de Partidos')
    plt.show()

    # 2. Separación entre clases (Violin Plot)
    # Comparamos la probabilidad asignada contra el resultado real
    resultados = pd.DataFrame({'Probabilidad': probs, 'Realidad': y_test})
    plt.figure(figsize=(8, 5))
    sns.violinplot(x='Realidad', y='Probabilidad', data=resultados, palette='coolwarm')
    plt.title('Separación entre Clases (Realidad vs Probabilidad)')
    plt.xticks([0, 1], ['Perdió', 'Ganó'])
    plt.show()

if __name__ == "__main__":
    ejecutar_diagnostico()